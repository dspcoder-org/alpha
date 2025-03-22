# Directories
SRC_DIR = src
INC_DIR = inc
LIB_DIR = lib

# Files
MAIN_SRC = $(SRC_DIR)/main.cpp
EXEC = a.out
LIB_OBJ = $(LIB_DIR)/libdspcoder.a  

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++20 -Wall -fPIC -Wno-return-type
INCLUDES = -I$(INC_DIR)

# Default target
all: $(EXEC)

# Rule to build the executable and link it with the static library
$(EXEC): $(MAIN_SRC) $(LIB_OBJ)
	$(CXX) $(CXXFLAGS) $(MAIN_SRC) $(INCLUDES) -L$(LIB_DIR) -ldspcoder -o $(EXEC)

# Clean up the build
clean:
	rm -f $(EXEC)