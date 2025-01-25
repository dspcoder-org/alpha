import sys
import shutil
import os
import subprocess


question_path = sys.argv[1]
lang = sys.argv[2]
work = sys.argv[3] if len(sys.argv) > 3 else "build"

build_sh_path = f"./build/build.sh"
c_makefile_path = f"./build/Makefile_c"  
cpp_makefile_path = f"./build/Makefile_cpp"  
build_target_dir = f"{question_path}/{lang}/._dev/"  
makefile_target_dir = f"{question_path}/{lang}/"


def execute_build_script(build_sh_path, target_dir):
    # Ensure the build.sh file exists
    if not os.path.exists(build_sh_path):
        raise FileNotFoundError(f"{build_sh_path} does not exist.")
    
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"{target_dir} does not exist.")
    
    # Copy build.sh to the target directory
    target_build_path = os.path.join(target_dir, "build.sh")
    shutil.copy(build_sh_path, target_build_path)

    # Make build.sh executable
    os.chmod(target_build_path, 0o755)

    # Execute build.sh in the target directory
    try:
        result = subprocess.run(
            ["./build.sh"],
            cwd=target_dir,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10  # Timeout after 10 seconds
        )
        # print("Script Output:")
        print(result.stdout)
        # print("Script Errors:")
        print(result.stderr)
        return result.returncode
    except subprocess.TimeoutExpired:
        print("Execution of build.sh timed out.")
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

def build():
    
    try:
        # Ensure the build.sh file exists
        if not os.path.exists(build_sh_path):
            raise FileNotFoundError(f"{build_sh_path} does not exist.")
        
        # Ensure the target directory exists
        if not os.path.exists(build_target_dir):
            raise FileNotFoundError(f"{build_target_dir} does not exist.")
        
        # Copy build.sh to the target directory
        target_build_path = os.path.join(build_target_dir, "build.sh")
        shutil.copy(build_sh_path, target_build_path)

        # Make build.sh executable
        os.chmod(target_build_path, 0o755)

        # Execute build.sh in the target directory
        try:
            result = subprocess.run(
                ["./build.sh"],
                cwd=build_target_dir,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10  # Timeout after 10 seconds
            )
            # print("Script Output:")
            print(result.stdout)
            # print("Script Errors:")
            print(result.stderr)
            return result.returncode
        except subprocess.TimeoutExpired:
            print("Execution of build.sh timed out.")
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 1
        
    except Exception as e:
        print(f"Failed to execute build.sh: {e}")
    
    
def clean():
    try:
        # remove make file it exists
        if os.path.exists(makefile_target_dir + "Makefile"):
            os.remove(makefile_target_dir + "Makefile")
        if os.path.exists(build_target_dir + "a.out"):
            os.remove(build_target_dir + "a.out")
        if os.path.exists(build_target_dir + "build.sh"):
            os.remove(build_target_dir + "build.sh")
        if os.path.exists(f"{question_path}/{lang}/lib/libdspcoder.a"):
            os.remove(f"{question_path}/{lang}/lib/libdspcoder.a")
        
        
    except Exception as e:
        print(f"Failed to remove Makefile: {e}")

def run_koro():
    # Command and arguments
    command = [
        "python3",
        "dev-koro.py",
        question_path,
        lang
    ]

    try:
        # Execute the command
        result = subprocess.run(
            command,
            text=True,                # Capture output as strings
            stdout=subprocess.PIPE,   # Capture standard output
            stderr=subprocess.PIPE    # Capture standard error
        )

        # Print the results
        print("Koro Output:")
        print(result.stdout)

        print("Koro Errors (if any):")
        print(result.stderr)

        return result.returncode

    except Exception as e:
        print(f"An error occurred while running the command: {e}")
        return 1
    
def make():
    build()
    try:
        if lang == "C":
            shutil.copy(c_makefile_path, makefile_target_dir + "Makefile") 
            shutil.move(f"{question_path}/{lang}/src/main.c", f"{question_path}/{lang}/src/temp.c")
            shutil.move(f"{question_path}/{lang}/._dev/main_dev.c", f"{question_path}/{lang}/src/main.c")
            
            # make build
            # Execute build.sh in the target directory
            try:
                result = subprocess.run(
                    ["./build.sh"],
                    cwd=target_dir,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=10  # Timeout after 10 seconds
                )
                # print("Script Output:")
                print(result.stdout)
                # print("Script Errors:")
                print(result.stderr)
                return result.returncode
            except subprocess.TimeoutExpired:
                print("Execution of build.sh timed out.")
                return 1
            except Exception as e:
                print(f"An error occurred: {e}")
                return 1
            
            shutil.move(f"{question_path}/{lang}/src/main.c", f"{question_path}/{lang}/._dev/main_dev.c")
            shutil.move(f"{question_path}/{lang}/src/temp.c", f"{question_path}/{lang}/src/main.c")
            
        elif lang == "Cpp":
            shutil.copy(cpp_makefile_path, makefile_target_dir + "Makefile")
            print("CPP Makefile copied") 
        
    except Exception as e:
        print(f"Failed to execute build.sh: {e}")


def generate():
    pass

# Example usage
if __name__ == "__main__":
    
    if work == "generate":
        generate()
        
    elif work == "build":
        build()
        
    elif work == "clean":
        clean()
        
    elif work == "koro":
        run_koro()
    
    elif work == "make":
        make()