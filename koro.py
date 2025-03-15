import subprocess
import threading
import os
import json
import sys
from typing import Any, Tuple, Optional
from time import time
import importlib.util
import inspect
from ValgrindAnalyzer import *


class Koro:
    def __init__(self, folderPath, lang, test_results_path):   
        self.submit_res = {"metadata": {}, "test_cases": {}}
        self.folderPath = folderPath
        self.lang = lang
        try:
            self.profiling = True if sys.argv[3] == 'p' else False
        except:
            self.profiling = False
        self.test_script_path = f"{folderPath}/._tests/test.py"
        self.test_executable = f"{folderPath}/{lang}/._dev/a.out"
        self.test_cases = None
        self.test_function_metadata = {}  # Store metadata for each test function
        self.load_test_cases()
        
        if not os.path.exists(self.test_executable):
            raise Exception("Executable not found.")
        
        self.__version__ = "0.0.1"
        self.path_to_save_result = test_results_path

    def truncate_string(self, s, max_length=50):
        """Helper function to truncate strings for logging."""
        if len(s) <= max_length:
            return s
        keep = (max_length - 3) // 2
        start = s[:keep]
        end = s[-keep:]
        return f"{start}...{end}"

    def load_test_cases(self):
        """Load test cases from a provided test script."""
        spec = importlib.util.spec_from_file_location("test_module", self.test_script_path)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
        setattr(test_module, "execute_bin", self.run_exe_with_input)
        self.test_cases = getattr(test_module, 'testCases')(self.test_executable)

        # Ensure required attributes exist in testCases
        if not all(hasattr(self.test_cases, attr) for attr in ['RUN', 'exe', 'default_timeout_window', 'usage']):
            raise AttributeError("TestCases class is missing required attributes.")
    

    def get_test_case_methods(self):
        """Get test case methods and their metadata."""
        test_case_methods = []
        for name, func in inspect.getmembers(self.test_cases, predicate=inspect.ismethod):
            if name.startswith('test_case'):
                # Extract timeout and override metadata for each test method
                sig = inspect.signature(func)
                timeout_window = sig.parameters.get('timeout_window').default if 'timeout_window' in sig.parameters else None
                override = sig.parameters.get('override').default if 'override' in sig.parameters else None

                self.test_function_metadata[name] = {
                    'timeout_window': timeout_window,
                    'override': override
                }

                test_case_methods.append(func)
        return test_case_methods

    def run_exe_with_input(self, input_data: Any, exe: str, timeout: int):
        """
        Run the executable with input and a timeout using subprocess's timeout feature.

        Args:
            input_data: Input to pass to the executable
            exe: Path to the executable
            timeout: Timeout in seconds for the execution

        Returns:
            Tuple of (output, error, execution_time)
        """
        # Validate the executable path
        if not exe or not os.path.exists(exe) or not os.access(exe, os.X_OK):
            return "", f"Invalid executable path or permissions: {exe}", 0

        # Convert input data to string
        input_str = '\n'.join(map(str, input_data)) + '\n' if isinstance(input_data, (list, tuple)) else f"{input_data}\n"

        # Start process with subprocess.Popen
        start_time = time()
        process = subprocess.Popen(
            [exe],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            preexec_fn=os.setsid  # Create a new process group
        )

        # Communicate with the process and apply the timeout
        try:
            stdout, stderr = process.communicate(input=input_str, timeout=timeout)
            execution_time = time() - start_time
            return stdout.strip(), stderr.strip() if stderr else None, execution_time
        except subprocess.TimeoutExpired:
            # Handle timeout: Kill the process and return timeout status
            process.kill()
            process.communicate()  # Wait for process termination
            execution_time = timeout
            return "Timed out", None, execution_time

    def run_tests(self):
        """Run all tests and collect results."""
        failFlag = False
        total_time = 0
        val_arg = None
        for test_method in self.get_test_case_methods():
            # Handle default and overridden tests
            override = self.test_function_metadata[test_method.__name__]["override"]
            if override == 0 or override is None:
                ip, expected = test_method()
                if val_arg == None:
                    val_arg = ip
                timeout = self.test_function_metadata[test_method.__name__]["timeout_window"] or self.test_cases.default_timeout_window
                out, err, exe_time = self.run_exe_with_input(input_data=ip, exe=self.test_executable, timeout=timeout)

                if err:
                    failFlag = True
                    self.submit_res["test_cases"][test_method.__name__] = {
                        "status": "FAIL", 
                        "executable output": self.truncate_string(out),
                        "expected output": self.truncate_string(expected),
                        "input": self.truncate_string(ip),
                        "error": err, 
                        "exe_time": exe_time,
                        "timeout": timeout,
                        "Override_Level": "0"
                    }
                else:
                    status = "PASS" if out == expected else "FAIL"
                    failFlag = failFlag or (status == "FAIL")
                    self.submit_res["test_cases"][test_method.__name__] = {
                        "status": status, 
                        "executable output": self.truncate_string(out),
                        "expected output": self.truncate_string(expected),
                        "input": self.truncate_string(ip),
                        "error": err,
                        "exe_time": exe_time,
                        "timeout": timeout,
                        "Override_Level": "0"
                    }

                total_time += exe_time

            elif override == 1:
                # Handle overridden tests (use threading for more control)
                timeout = self.test_function_metadata[test_method.__name__]["timeout_window"] or self.test_cases.default_timeout_window
                execution_time = 0
                completed = threading.Event()
                result = [None]

                def run_test():
                    try:
                        result[0] = test_method()
                    except Exception as e:
                        result[0] = str(e)
                    finally:
                        completed.set()

                # Start the test in a thread
                thread = threading.Thread(target=run_test)
                thread.daemon = True
                thread.start()

                # Wait for test completion or timeout
                completed.wait(timeout=timeout / 1000)
                execution_time = time() * 1000 - total_time

                if completed.is_set():
                    status = "PASS" if result[0] else "FAIL"
                    self.submit_res["test_cases"][test_method.__name__] = {
                        "Override_Level": "1",
                        "status": status,
                        "error": result[0]
                    }
                else:
                    self.submit_res["test_cases"][test_method.__name__] = {
                        "Override_Level": "1",
                        "status": "FAIL",
                        "error": "Execution timed out"
                    }
                    failFlag = True

                total_time += execution_time

        self.submit_res["metadata"].update({"Total_Time": total_time, "overall_status": "FAIL" if failFlag else "PASS"})

        # final valgrind check 
        memStat = {}
        if self.profiling:
            if isinstance(val_arg, (list, tuple)):
                val_arg = '\n'.join(map(str, val_arg)) + '\n'
            else:
                val_arg = f"{str(val_arg)}\n"
            analyzer = ValgrindAnalyzer(self.test_executable, input=val_arg)
            memStat = {"footprint": analyzer.get_memory_footprint(), "memory_leak":analyzer.check_memory_leaks(), "cache_profile":analyzer.get_cache_profile()}
        self.submit_res["metadata"]["mem_stat"] = memStat

        # saving Submit results in /dspcoder/results
        with open(f'{self.path_to_save_result}/{os.path.basename(self.folderPath)}_{self.lang}.json', 'w') as file:
            json.dump(self.submit_res, file, indent=4)


#######################
#   Koror driver code #
#######################

if __name__ == "__main__":
    
    folderPath = sys.argv[1]
    lang = sys.argv[2]
    test_results_path = "./koro_output/"

    try:
        tester = Koro(folderPath, lang, test_results_path)
        tester.run_tests()
    except Exception as e:
        print(f"Koro failed: {e}") 
