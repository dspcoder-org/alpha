#include "util.hpp"
#include <vector>
#include <iostream>

bool detect_cycle(LinkedList* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head);

    // Print the result
    std::cout << (has_cycle ? "true" : "false") << std::endl;

    return 0;
}