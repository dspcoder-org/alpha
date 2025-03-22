#include <iostream>
#include <cstdlib>

// Function declarations
void* aligned_malloc(size_t size, size_t alignment);

// Function to allocate aligned memory
void* aligned_malloc(size_t size, size_t alignment) {
    void* ptr = nullptr;
    if (posix_memalign(&ptr, alignment, size) != 0) {
        return nullptr;
    }
    return ptr;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cout << "Usage: " << argv[0] << " <size> <alignment>\n";
        return 1;
    }

    size_t size = std::stoi(argv[1]);
    size_t alignment = std::stoi(argv[2]);

    void* ptr = aligned_malloc(size, alignment);
    if (ptr == nullptr) {
        std::cout << "Memory allocation failed\n";
        return 1;
    }

    std::cout << "Allocated memory at: " << ptr << "\n";
    free(ptr);
    return 0;
}