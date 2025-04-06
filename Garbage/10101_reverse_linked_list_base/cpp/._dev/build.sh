#!/bin/bash

# Get the directory containing the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set up directories and files for main build
SRC_DIR="."
LIB_DIR="../lib"
EXEC_DIR="."
MAIN_SRC="${SRC_DIR}/main_dev.cpp ${SRC_DIR}/solution_dev.cpp"
LIB_OBJ="${LIB_DIR}/libdspcoder.a"
EXEC="${EXEC_DIR}/a.out"

# Set up library source files
LIB_SRC="./lib.cpp"
OBJ_FILE="${LIB_DIR}/libdspcoder.o"

# Compiler settings
CC="g++"
CFLAGS="-Wall -fPIC -Wno-format-zero-length -std=c++11 -g"

# Function to build library
build_lib() {
    # Create the lib directory if it doesn't exist
    mkdir -p ${LIB_DIR}
    
    # Check if the source file exists
    if [ ! -f "${LIB_SRC}" ]; then
        echo "Source file ${LIB_SRC} not found!"
        exit 1
    fi
    
    # Remove old library if it exists
    rm -f ${LIB_OBJ}
    
    # Compile the object file
    ${CC} ${CFLAGS} -c ${LIB_SRC} -o ${OBJ_FILE}
    
    # Create the static library
    ar rcs ${LIB_OBJ} ${OBJ_FILE}
    
    # Clean up object file
    rm -f ${OBJ_FILE}
    echo "Static library created at ${LIB_OBJ}"
}

# Function to build main program
build_main() {
    ${CC} ${CFLAGS} ${MAIN_SRC} -L${LIB_DIR} -ldspcoder -o ${EXEC}
    echo "Build complete: ${EXEC}"
}

# Function to clean
clean() {
    echo "Cleaning..."
    rm -f ${EXEC} ${LIB_OBJ} ${OBJ_FILE}
}

# Command handling
case "$1" in
    "lib")
        build_lib
        ;;
    "build")
        build_main
        ;;
    "clean")
        clean
        ;;
    *)
        # Default: build both library and main program
        clean
        build_lib
        build_main
        ;;
esac
