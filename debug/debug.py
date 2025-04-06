import sys
import os
import shutil

code_path = "./code"
if not os.path.exists(code_path):
    os.makedirs(code_path)
    
if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    print("Expected : python debug.py question_path lang")
    sys.exit(1)

question_path = sys.argv[1].rstrip("/")

lang = sys.argv[2]

file = {
    "lib.c" : {
        "code" : f"{question_path}/c/._dev/lib.c",
        "debug_path" : f"{code_path}/lib/lib.c",
    },
    "lib.cpp" : {
        "code" : f"{question_path}/cpp/._dev/lib.cpp",
        "debug_path" : f"{code_path}/lib/lib.cpp",
    },
    "main.c" : {
        "code" : f"{question_path}/c/._dev/main_dev.c",
        "debug_path" : f"{code_path}/src/main.c",
    },
    "main.cpp" : {
        "code" : f"{question_path}/cpp/._dev/main_dev.cpp",
        "debug_path" : f"{code_path}/src/main.cpp",
    },
    "util.h" : {
        "code" : f"{question_path}/c/inc/util.h",
        "debug_path" : f"{code_path}/inc/util.h",
    },
    "util.hpp" : {
        "code" : f"{question_path}/cpp/inc/util.hpp",
        "debug_path" : f"{code_path}/inc/util.hpp",
    },
    "launch.json" : {
        "code" : f"{question_path}/{lang.lower()}/.vscode/launch.json",
        "debug_path" : f"{code_path}/.vscode/launch.json",
    },
    "task.json" : {
        "code" : f"{question_path}/{lang.lower()}/.vscode/tasks.json",
        "debug_path" : f"{code_path}/.vscode/tasks.json",
    }
}

if lang.lower() == "c":
    files_to_copy = ["lib.c", "main.c", "util.h", "launch.json", "task.json"]
elif lang.lower() == "cpp": 
    files_to_copy = ["lib.cpp", "main.cpp", "util.hpp", "launch.json", "task.json"]
else:
    print("Error: Unsupported language. Please use 'c' or 'cpp'.")
    sys.exit(1)

for file_key in files_to_copy:
    # delete existing file in debug path
    if os.path.exists(file[file_key]["debug_path"]):
        os.remove(file[file_key]["debug_path"])
    # copy file from question path to debug path
    shutil.copy(file[file_key]["code"], file[file_key]["debug_path"])

# Makefile
# remove existing mske file
makefile_path = f"{code_path}/Makefile"
if os.path.exists(makefile_path):
    os.remove(makefile_path)
if lang.lower() == "c":
    # Create a copy of makefile_c in code_path to Makefile in code_path
    shutil.copy(f"{code_path}/makefile_c.txt", makefile_path)
elif lang.lower() == "cpp":
    # Create a copy of makefile_cpp in code_path to Makefile in code_path
    shutil.copy(f"{code_path}/makefile_cpp.txt", makefile_path)
else:
    print("Error: Unsupported language. Please use 'c' or 'cpp'.")
    


