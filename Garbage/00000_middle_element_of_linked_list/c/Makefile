# Directories
SRC_DIR = src
INC_DIR = inc
LIB_DIR = lib
EXE_DIR = .

# Files
MAIN_SRC = $(SRC_DIR)/main.c
LIB_OBJ = $(LIB_DIR)/libdspcoder.a  # Change to .a for static library
EXEC = $(EXE_DIR)/a.out

# Compiler and flags
CC = gcc
CFLAGS = -Wall -fPIC -Wno-return-type -g    # Flags for the compiler
INCLUDES = -I$(INC_DIR)  # Include directories

# Default target
all: $(EXEC)

# Rule to build the executable and link it with the static library
$(EXEC): $(MAIN_SRC) $(LIB_OBJ)
	$(CC) $(CFLAGS) $(MAIN_SRC) $(INCLUDES) -L$(LIB_DIR) -ldspcoder -o $(EXEC)

# Clean up the build
clean:
	rm -f $(EXEC)
