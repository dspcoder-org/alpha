#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function prototypes
extern void* aligned_malloc(size_t size, size_t alignment);

void* aligned_malloc(size_t size, size_t alignment) {
    void* ptr = NULL;
    if (posix_memalign(&ptr, alignment, size) != 0) {
        return NULL;
    }
    return ptr;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: %s <size> <alignment>\n", argv[0]);
        return 1;
    }

    size_t size = atoi(argv[1]);
    size_t alignment = atoi(argv[2]);

    void* ptr = aligned_malloc(size, alignment);
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Allocated memory at: %p\n", ptr);
    free(ptr);
    return 0;
}