# inp : question_ folder and location of build_files 
# copy from build files to question

import os
import shutil
import subprocess

class build:
    def __init__(self, question_path, build_files_path, vscode_files_path, base_question_path):
        self.build_files = build_files_path
        self.question_path = question_path
        self.vscode_files = vscode_files_path
        self.base_question_path = base_question_path
    
    def copy_build_files(self):
        
        print("============= Copy build files ============= ")
        
        # build_c.sh
        # check if it exist 
        build_c_path = f"{self.build_files}/build_c.sh"
        if not os.path.exists(build_c_path):
            raise FileNotFoundError(f"{build_c_path} does not exist.")
        # copy to question folder
        target_build_c_path = os.path.join(self.question_path, "c/._dev/build.sh")
        shutil.copy(build_c_path, target_build_c_path)
        os.chmod(target_build_c_path, 0o755)
        
        # build_cpp.sh
        # check if it exist
        build_cpp_path = f"{self.build_files}/build_cpp.sh"
        if not os.path.exists(build_cpp_path):
            raise FileNotFoundError(f"{build_cpp_path} does not exist.")
        # copy to question folder
        target_build_cpp_path = os.path.join(self.question_path, "cpp/._dev/build.sh")
        shutil.copy(build_cpp_path, target_build_cpp_path)
        os.chmod(target_build_cpp_path, 0o755)
        
        
        # Makefile_c
        # check if it exist
        makefile_c_path = f"{self.build_files}/Makefile_c"
        if not os.path.exists(makefile_c_path):
            raise FileNotFoundError(f"{makefile_c_path} does not exist.")
        # copy to question folder
        target_makefile_c_path = os.path.join(self.question_path, "c/Makefile")
        shutil.copy(makefile_c_path, target_makefile_c_path)

        # Makefile_cpp
        # check if it exist
        makefile_cpp_path = f"{self.build_files}/Makefile_cpp"
        if not os.path.exists(makefile_cpp_path):
            raise FileNotFoundError(f"{makefile_cpp_path} does not exist.")
        # copy to question folder
        target_makefile_cpp_path = os.path.join(self.question_path, "cpp/Makefile")
        shutil.copy(makefile_cpp_path, target_makefile_cpp_path)
        
        print("============= Done ============= \n")
        
    
    def copy_vscode_files(self):
        
        print("============= Copy vscode files ============= ")
        
        # copy settings.json and task.json from .vscode folder to question folder for c and cpp
        # copy one file at a time
        try:
            # c
            vscode_c_path = f"{self.vscode_files}c"
            if not os.path.exists(vscode_c_path):
                raise FileNotFoundError(f"{vscode_c_path} does not exist.")
            target_vscode_c_path = os.path.join(self.question_path, "c/.vscode")
            # copy settings.json
            shutil.copy(os.path.join(vscode_c_path, "settings.json"), os.path.join(target_vscode_c_path, "settings.json"))
            # copy tasks.json
            shutil.copy(os.path.join(vscode_c_path, "tasks.json"), os.path.join(target_vscode_c_path, "tasks.json"))
            
            # cpp
            vscode_cpp_path = f"{self.vscode_files}cpp"
            if not os.path.exists(vscode_cpp_path):
                raise FileNotFoundError(f"{vscode_cpp_path} does not exist.")
            target_vscode_cpp_path = os.path.join(self.question_path, "cpp/.vscode")
            # copy settings.json
            shutil.copy(os.path.join(vscode_cpp_path, "settings.json"), os.path.join(target_vscode_cpp_path, "settings.json"))
            # copy tasks.json
            shutil.copy(os.path.join(vscode_cpp_path, "tasks.json"), os.path.join(target_vscode_cpp_path, "tasks.json"))
            
            # limits.json
            limits_path = f"{self.base_question_path }._tests/limits.json"
            if not os.path.exists(limits_path):
                raise FileNotFoundError(f"{limits_path} does not exist.")
            target_limits_path = os.path.join(self.question_path, "._tests/limits.json")
            shutil.copy(limits_path, target_limits_path)
            
        except Exception as e:
            print(f"An error occurred while copying vscode files: {e}")
        print("============= Done ============= \n")
    
    def build_c(self):
        # Execute build.sh in the target directory
        try:
            result = subprocess.run(
                ["./build.sh"],
                cwd=os.path.join(self.question_path, "c/._dev"),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # Timeout after 10 seconds
            )
            # print("Script Output:")
            if result.stdout:
                print(result.stdout)
                
            # print("Script Errors:")
            if result.stderr:
                print(result.stderr)
                
            return result.returncode
        except subprocess.TimeoutExpired:
            print("Execution of build.sh timed out in c.")
            return 1
        except Exception as e:
            print(f"An error occurred while building c: {e}")
            return 1
    
    def build_cpp(self):
        # Execute build.sh in the target directory
        try:
            result = subprocess.run(
                ["./build.sh"],
                cwd=os.path.join(self.question_path, "cpp/._dev"),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # Timeout after 10 seconds
            )
            # print("Script Output:")
            if result.stdout:
                print(result.stdout)
                
            # print("Script Errors:")
            if result.stderr:
                print(result.stderr)
            
            return result.returncode
        except subprocess.TimeoutExpired:
            print("Execution of build.sh timed out in cpp.")
            return 1
        except Exception as e:
            print(f"An error occurred while building cpp: {e}")
            return 1
        
    def build(self):
        print("============= Build ============= ")
        self.build_c()
        self.build_cpp()
        print("============= Done ============= \n")
        
        
    def remove_build_files(self):
        print("============= Remove build files ============= ")
        
        # remove build files from question folder
        try:
            if os.path.exists(os.path.join(self.question_path, "c/Makefile")):
                os.remove(os.path.join(self.question_path, "c/Makefile"))
            if os.path.exists(os.path.join(self.question_path, "cpp/Makefile")):
                os.remove(os.path.join(self.question_path, "cpp/Makefile"))
            if os.path.exists(os.path.join(self.question_path, "c/._dev/build.sh")):
                os.remove(os.path.join(self.question_path, "c/._dev/build.sh"))
            if os.path.exists(os.path.join(self.question_path, "cpp/._dev/build.sh")):
                os.remove(os.path.join(self.question_path, "cpp/._dev/build.sh"))
                
        except Exception as e:
            print(f"An error occurred while removing build files: {e}")
            print("============= Done ============= \n")
            return 1
        
        print("============= Done ============= \n")
        
        
    def clean(self):
        print("============= Clean ============= ")
        
        try:
            if os.path.exists(os.path.join(self.question_path, "c/lib/libdspcoder.a")):
                os.remove(os.path.join(self.question_path, "c/lib/libdspcoder.a"))
            if os.path.exists(os.path.join(self.question_path, "cpp/lib/libdspcoder.a")):
                os.remove(os.path.join(self.question_path, "cpp/lib/libdspcoder.a"))
            
            if os.path.exists(os.path.join(self.question_path, "c/._dev/a.out")):
                os.remove(os.path.join(self.question_path, "c/._dev/a.out"))
            if os.path.exists(os.path.join(self.question_path, "cpp/._dev/a.out")):
                os.remove(os.path.join(self.question_path, "cpp/._dev/a.out"))
            if os.path.exists(os.path.join(self.question_path, "c/a.out")):
                os.remove(os.path.join(self.question_path, "c/a.out"))
            if os.path.exists(os.path.join(self.question_path, "cpp/a.out")):
                os.remove(os.path.join(self.question_path, "cpp/a.out"))
            
        except Exception as e:
            print(f"An error occurred while cleaning build files: {e}")
            print("============= Done ============= \n")
            return 1
        
        print("============= Done ============= \n")
        
        
    def test_make_c(self):
        # Execute make in the target directory
        try:
            result = subprocess.run(
                ["make"],
                cwd=os.path.join(self.question_path, "c"),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # Timeout after 10 seconds
            )
            # print("Script Output:")
            if result.stdout:
                print(result.stdout)
                
            # print("Script Errors:")
            if result.stderr:
                print(result.stderr)
            
        except subprocess.TimeoutExpired:
            print("Execution of make timed out in c.")
            return 1
        except Exception as e:
            print(f"An error occurred while testing make in c: {e}")
            return 1
        
        # if os.path.exists(os.path.join(self.question_path, "c/a.out")):
        #     os.remove(os.path.join(self.question_path, "c/a.out"))
        # else:
        #     print("a.out does not exist in c")
                
        return result.returncode
        
    def test_make_cpp(self):
        # Execute make in the target directory
        try:
            result = subprocess.run(
                ["make"],
                cwd=os.path.join(self.question_path, "cpp"),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # Timeout after 10 seconds
            )
            # print("Script Output:")
            if result.stdout:
                print(result.stdout)
                
            # print("Script Errors:")
            if result.stderr:
                print(result.stderr)
            
        except subprocess.TimeoutExpired:
            print("Execution of make timed out in cpp.")
            return 1
        except Exception as e:
            print(f"An error occurred while testing make in cpp: {e}")
            return 1
        
        # if os.path.exists(os.path.join(self.question_path, "cpp/a.out")):
        #     os.remove(os.path.join(self.question_path, "cpp/a.out"))
        # else:
        #     print("a.out does not exist in cpp")
        
        return result.returncode