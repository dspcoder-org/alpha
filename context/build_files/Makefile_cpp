# ============================================================
# ================== DO NOT MODIFY THIS MAKEFILE =============
# ============================================================

# Directories
SRC_DIR = src
INC_DIR = inc
LIB_DIR = lib
EXE_DIR = .

# Files
MAIN_SRC = $(SRC_DIR)/*.cpp       # All C++ source files in the source directory
LIB_OBJ = $(LIB_DIR)/libdspcoder.a  # Static library file
EXEC = $(EXE_DIR)/a.out         # Name of the output executable

# Compiler and flags
CXX = g++                         # Compiler to be used
CXXFLAGS = -std=c++20 -Wall -fPIC -Wno-return-type -g  # Compiler flags for C++20, warnings, debugging, etc.
INCLUDES = -I$(INC_DIR)           # Include directory for header files

# Default target to build the executable
all: $(EXEC)

# Rule to build the executable and link it with the static library
$(EXEC): $(MAIN_SRC) $(LIB_OBJ)
	$(CXX) $(CXXFLAGS) $(MAIN_SRC) $(INCLUDES) -L$(LIB_DIR) -ldspcoder -o $(EXEC)

# Clean up the build by removing the executable
clean:
	rm -f $(EXEC)