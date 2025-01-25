# sys.argv[1] = path upto questionID folder
# sys.argv[2] = lang
# sys.argv[3] = p for profiling result or empty  


from typing import Union, Tuple, Any, Optional
import importlib.util
import inspect, sys, re, os
from time import time
from threading import Timer
from ValgrindAnalyzer import *
import subprocess, threading
import signal, json
from config import * 


class TimeoutException(Exception):
    """Custom exception for handling timeouts."""
    print("Timeout reachennmnd")
    pass


def alarm_handler(signum, frame):
    """Signal handler for the timeout alarm."""
    raise TimeoutException("Timeout reached")

# Set the global signal handler for the timeout
signal.signal(signal.SIGALRM, alarm_handler)

if len(sys.argv) < 2:
    raise Exception(" USAGE: \n\
        # sys.argv[1] = path upto questionID folder \n\
        # sys.argv[2] = lang \n\
        # sys.argv[3] = p for profiling result or leave blank \n")

class Koro:
    def __init__(self, folderPath=sys.argv[1], lang=sys.argv[2]):
        self.submit_res = {"metadata": {}, "test_cases": {}}
        self.folderPath = folderPath
        self.lang=lang
        try:
            self.profiling = True if sys.argv[3] == 'p' else False
        except:
            self.profiling = False
        self.test_script_path = f"{folderPath}/._tests/test.py"
        self.test_executable = f"{folderPath}/{lang}/._dev/a.out"
        
        self.test_cases = None
        self.test_function_metadata = {}  # Store metadata for each test function
        self.load_test_cases()
        
        if os.path.exists(self.test_executable):
            pass
        else:
            raise Exception ("executable not found.")
        self.__version__ = "0.0.1"

    def truncate_string(self, s, max_length=50):
        if len(s) <= max_length:
            return s
        
        # Calculate how many characters to keep at the start and end
        keep = (max_length - 3) // 2
        start = s[:keep]
        end = s[-keep:]
        
        # Add "..." to indicate truncation
        return f"{start}...{end}"

    def load_test_cases(self):
        # Load the module from the specified file path
        spec = importlib.util.spec_from_file_location("test_module", self.test_script_path)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)
        
        # Access the testCases class from the module
        setattr(test_module, "execute_bin", self.run_exe_with_input)
        self.test_cases = getattr(test_module, 'testCases')(self.test_executable)
        
        # Ensure RUN, exe, and default_timeout_window attributes exist in testCases
        if not all(hasattr(self.test_cases, attr) for attr in ['RUN', 'exe', 'default_timeout_window', 'usage']):
            raise AttributeError("The testCases class must have RUN, exe, default_timeout_window attributes, and usage.")
        
        # if self.test_cases.usage != 'dev':
        #     raise Exception("dev-koro: Test file is in used for development the usage must be set to 'dev' in testCase init.")


    def get_test_case_methods(self):
        """
        Get all methods in testCases class that start with 'test_case' and extract metadata.
        """
        test_case_methods = []
        
        for name, func in inspect.getmembers(self.test_cases, predicate=inspect.ismethod):
            if name.startswith('test_case'):
                # Extract default parameter values for timeout_window and override if available
                sig = inspect.signature(func)
                timeout_window = sig.parameters.get('timeout_window').default if 'timeout_window' in sig.parameters else None
                override = sig.parameters.get('override').default if 'override' in sig.parameters else None

                # Store metadata for future use
                self.test_function_metadata[name] = {
                                                        'timeout_window': timeout_window,
                                                        'override': override
                                                    }

                test_case_methods.append(func)

        return test_case_methods

    # def run_exe_with_input(self, input_data: Any, exe: str, timeout: Optional[float] = None) -> Tuple[str, str, float]:
    #     """
    #     Run a compiled executable with provided input data using both signal-based and subprocess timeout mechanisms.

    #     Args:
    #         input_data: Input data of any type to be passed to the executable
    #         exe: Path to the executable
    #         timeout: Maximum execution time in milliseconds (default: None, uses 5000ms)

    #     Returns:
    #         Tuple[str, str, float]: (output, error, execution_time)
    #             - output: Program output or error message
    #             - error: Error message if any, None otherwise
    #             - execution_time: Execution time in milliseconds
    #     """
    #     # Input validation
    #     if not exe or not isinstance(exe, str):
    #         return "", "Invalid executable path", 0
        
    #     if not os.path.exists(exe):
    #         return "", f"Executable not found: {exe}", 0
        
    #     if not os.access(exe, os.X_OK):
    #         return "", f"Permission denied: {exe}", 0

    #     # Convert input data to string format with proper error handling
    #     try:
    #         if isinstance(input_data, (list, tuple)):
    #             input_str = '\n'.join(map(str, input_data)) + '\n'
    #         else:
    #             input_str = f"{str(input_data)}\n"
    #     except Exception as e:
    #         return "", f"Input data conversion error: {str(e)}", 0

    #     # Initialize variables
    #     process = None
    #     output = ""
    #     err = None
    #     execution_time = 0
    #     timeout_secs = timeout  
    #     # timeout_secs = 500000  # Convert ms to seconds, default 5s
    #     timeout_occurred = False

    #     def timeout_handler(signum, frame):
    #         """Signal handler for the timeout alarm."""
    #         nonlocal timeout_occurred
    #         timeout_occurred = True
    #         print("Timeout reached")
    #         if process:
    #             try:
    #                 os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    #             except:
    #                 pass
    #         raise TimeoutException("Timeout reached")

    #     # Set up signal handler
    #     original_handler = signal.signal(signal.SIGALRM, timeout_handler)

    #     try:
    #         # Start process with stricter parameters
    #         process = subprocess.Popen(
    #             [exe],
    #             stdin=subprocess.PIPE,
    #             stdout=subprocess.PIPE,
    #             stderr=subprocess.PIPE,
    #             text=True,
    #             shell=True,
    #             preexec_fn=os.setsid,  # Create new process group
    #             env=os.environ.copy()   # Use clean environment
    #         )

    #         # Set up both timeouts
    #         signal.setitimer(signal.ITIMER_REAL, timeout_secs)
    #         start_time = time() * 1000

    #         try:
    #             # Use communicate with timeout as a backup
    #             stdout, stderr = process.communicate(input=input_str, timeout=timeout_secs)
    #             execution_time = (time() * 1000) - start_time
    #             output = stdout.strip()
    #             err = stderr.strip() if stderr else None
    #             print("Execution time:", execution_time)
    #             print("timeout_secs:", timeout_secs)

    #         except (subprocess.TimeoutExpired, TimeoutException):
    #             print("Timeout occurred")
    #             timeout_occurred = True
    #             # Handle timeout by terminating the process group
    #             try:
    #                 os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    #                 # Give it 1 second to terminate gracefully
    #                 process.wait(timeout=1)
    #             except:
    #                 try:
    #                     # Force kill if still running
    #                     os.killpg(os.getpgid(process.pid), signal.SIGKILL)
    #                 except:
    #                     pass
                
    #             output = "Timed out"
    #             execution_time = timeout  # Return the full timeout duration

    #     except FileNotFoundError:
    #         output = ""
    #         err = f"Executable '{exe}' not found"
        
    #     except PermissionError:
    #         output = ""
    #         err = f"Permission denied to execute '{exe}'"
        
    #     except Exception as e:
    #         output = ""
    #         err = f"Execution error: {str(e)}"

    #     finally:
    #         # Reset signal handler and timer
    #         signal.signal(signal.SIGALRM, original_handler)
    #         signal.setitimer(signal.ITIMER_REAL, 0)

    #         # Ensure process cleanup
    #         if process:
    #             try:
    #                 if process.poll() is None:
    #                     # If process is still running, force kill it
    #                     os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                    
    #                 # Close file descriptors
    #                 if process.stdout:
    #                     process.stdout.close()
    #                 if process.stderr:
    #                     process.stderr.close()
    #                 if process.stdin:
    #                     process.stdin.close()
                    
    #                 process.kill()
    #                 process.wait(timeout=1)
    #             except:
    #                 pass

    #         # If timeout occurred but we somehow got here without proper cleanup
    #         if timeout_occurred and not output:
    #             output = "Timed out"
    #             execution_time = timeout or 5000

    #     return output, err, execution_time
    
    # timeout is not optional
    def run_exe_with_input(self, input_data: Any, exe: str, timeout: int):
        """
        Run a compiled executable with provided input data using subprocess timeout mechanism.

        Args:
            input_data: Input data of any type to be passed to the executable
            exe: Path to the executable
            timeout: Maximum execution time in seconds (default: None, uses 5 seconds)

        Returns:
            Tuple[str, str, float]: (output, error, execution_time)
                - output: Program output or error message
                - error: Error message if any, None otherwise
                - execution_time: Execution time in seconds
        """
        # Input validation
        if not exe or not isinstance(exe, str):
            return "", "Invalid executable path", 0
        
        if not os.path.exists(exe):
            return "", f"Executable not found: {exe}", 0
        
        if not os.access(exe, os.X_OK):
            return "", f"Permission denied: {exe}", 0

        # Convert input data to string format with proper error handling
        try:
            if isinstance(input_data, (list, tuple)):
                input_str = '\n'.join(map(str, input_data)) + '\n'
            else:
                input_str = f"{str(input_data)}\n"
        except Exception as e:
            return "", f"Input data conversion error: {str(e)}", 0

        # Initialize variables
        output = ""
        err = None
        execution_time = 0
        timeout_secs = timeout if timeout is not None else 5  # Default to 5 seconds if no timeout is provided

        try:
            # Start process with stricter parameters
            process = subprocess.Popen(
                [exe],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True,
                preexec_fn=os.setsid,  # Create new process group
                env=os.environ.copy()   # Use clean environment
            )

            start_time = time()

            try:
                # Use communicate with timeout
                stdout, stderr = process.communicate(input=input_str, timeout=timeout_secs)
                execution_time = time() - start_time
                output = stdout.strip()
                err = stderr.strip() if stderr else None
            except subprocess.TimeoutExpired:
                # Handle timeout by terminating the process
                process.kill()
                stdout, stderr = process.communicate()
                execution_time = timeout_secs
                output = "Timed out"
                err = stderr.strip() if stderr else None

        except FileNotFoundError:
            output = ""
            err = f"Executable '{exe}' not found"
        
        except PermissionError:
            output = ""
            err = f"Permission denied to execute '{exe}'"
        
        except Exception as e:
            output = ""
            err = f"Execution error: {str(e)}"

        finally:
            # Ensure process cleanup
            if process:
                try:
                    if process.poll() is None:
                        # If process is still running, force kill it
                        os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                    
                    # Close file descriptors
                    if process.stdout:
                        process.stdout.close()
                    if process.stderr:
                        process.stderr.close()
                    if process.stdin:
                        process.stdin.close()
                    
                    process.kill()
                    process.wait(timeout=1)
                except:
                    pass

        return output, err, execution_time

    def run_tests(self):
        failFlag = False
        val_arg = None
        TT = 0
        for test_method in self.get_test_case_methods():
            # override = 0
            if self.test_function_metadata[test_method.__name__]["override"] == 0 or self.test_function_metadata[test_method.__name__]["override"] == None:
                ip, expected = test_method()
                if val_arg == None:
                    val_arg = ip
                timeout = self.test_function_metadata[test_method.__name__]["timeout_window"] or self.test_cases.default_timeout_window
                out, err, exe_time = self.run_exe_with_input(input_data=ip, exe=self.test_executable, timeout=timeout)

                if err:
                    self.submit_res["test_cases"][test_method.__name__]={
                                                                            "status": "FAIL", 
                                                                            "executable output": f"{self.truncate_string(out)}",
                                                                            "expected   output": f"{self.truncate_string(expected)}",
                                                                            "input": f"{self.truncate_string(ip)}",
                                                                            "error": f"{err}", 
                                                                            "exe_time": f"{exe_time}",
                                                                            "timeout" : f"{timeout}",
                                                                            "Override_Level": "0"
                                                                            }
                    failFlag = True
                else:
                    if out == expected:
                        self.submit_res["test_cases"][test_method.__name__]={
                                                                            "status": "PASS", 
                                                                            "executable output": f"{self.truncate_string(out)}",
                                                                            "expected   output": f"{self.truncate_string(expected)}",
                                                                            "input": f"{self.truncate_string(ip)}",
                                                                            "error": f"{err}",
                                                                            "exe_time": f"{exe_time}",
                                                                            "timeout" : f"{timeout}",
                                                                            "Override_Level": "0"
                                                                            }
                    else:
                        self.submit_res["test_cases"][test_method.__name__]={
                                                                            "status": "FAIL",
                                                                            "executable output": f"{self.truncate_string(out)}",
                                                                            "expected   output": f"{self.truncate_string(expected)}",
                                                                            "input": f"{self.truncate_string(ip)}",
                                                                            "error": f"{err}",
                                                                            "exe_time": f"{exe_time}",
                                                                            "timeout" : f"{timeout}",
                                                                            "Override_Level": "0",
                                                                            }
                        failFlag = True
                TT+=exe_time

            # override = 1
            elif self.test_function_metadata[test_method.__name__]["override"] == 1:
                timeout = self.test_function_metadata[test_method.__name__]["timeout_window"] or self.test_cases.default_timeout_window
                execution_time = 0

                # Create an Event for thread synchronization
                completed = threading.Event()
                result = [None]
                error_occurred = [False]

                def run_test(self):
                    try:
                        result[0] = test_method()
                        completed.set()
                    except Exception as e:
                        error_occurred[0] = True
                        result[0] = str(e)
                        completed.set()

                thread = threading.Thread(target=run_test, args=(self,))
                thread.daemon = True  # Mark as daemon so it won't prevent program exit
                
                start_time = time() * 1000

                thread.start()
                # Wait for either completion or timeout
                completed.wait(timeout=timeout/1000)  # Convert ms to seconds

                execution_time = time() * 1000 - start_time

                if completed.is_set():
                    if error_occurred[0]:
                        self.submit_res["test_cases"][test_method.__name__]={"Override_Level": "1",
                                                                            "status": "FAIL",
                                                                            "error": f"{error_occurred[0]}"}
                        failFlag = True
                    else:
                        test_passed = result[0]
                        self.submit_res["test_cases"][test_method.__name__]={"Override_Level": "1",
                                                                            "status": "PASS" if test_passed else "FAIL",
                                                                            "erroe": f"{error_occurred[0]}"}
                        if not test_passed:
                            failFlag = True
                            self.submit_res["test_cases"][test_method.__name__]={"Override_Level": "1",
                                                                                "status": "FAIL",
                                                                                "error": f"{error_occurred[0]}"}
                else:
                    # Timeout occurred
                    self.submit_res["test_cases"][test_method.__name__]={"Override_Level": "1",
                                                                        "status": "FAIL",
                                                                        "error": f"Execution timed out",
                                                                        "Timeout": f"Execution Timedout"}
                    failFlag = True
                    execution_time = timeout

                TT+=execution_time

        self.submit_res["metadata"].update({"Total_Time": TT, "overall_status": "FAIL" if failFlag else "PASS"})

        
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
        with open(f'{path_to_save_result}/{os.path.basename(self.folderPath)}_{self.lang}.json', 'w') as file:
            json.dump(self.submit_res, file, indent=4)



#######################
#   Koror driver code #
#######################
try:
    tester = Koro()
    tester.run_tests()
except Exception as e:
    print(" USAGE: \n\
        # sys.argv[1] = path upto questionID folder \n\
        # sys.argv[2] = lang \n\
        # sys.argv[3] = p for profiling result or leave blank \n")
    
    print(e)

