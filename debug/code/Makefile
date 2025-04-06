# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -g -O0

# Source files and output
SRC = src/main.c lib/lib.c
OBJ = $(SRC:.c=.o)
TARGET = a.out

# Default target
all: $(TARGET)

# Linking
$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

# Compiling
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Dependencies
src/main.o: src/main.c inc/util.h
lib/lib.o: lib/lib.c inc/util.h

# Phony targets
.PHONY: clean debug run

# Clean build files
clean:
	rm -f $(OBJ) $(TARGET)

# Debug target - run with gdb
debug: $(TARGET)
	gdb ./$(TARGET)

# Run the program
run: $(TARGET)
	./$(TARGET)