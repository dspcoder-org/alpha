#include "../inc/util.hpp"
#include <vector>
#include <iostream>

bool detect_cycle(LinkedList* head) {
    // Write your code here
    
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to detect cycle in the linked list
    bool hasCycle = detect_cycle(head);

    // Print the result
    if (hasCycle) {
        std::cout << "true" << std::endl;
    } else {
        std::cout << "false" << std::endl;
    }

    return 0;
}