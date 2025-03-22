#include "util.hpp"
#include <vector>
#include <iostream>

int find_middle_element(LinkedList* head) {
    // Write your code here
    return 0; // Placeholder return
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to find the middle element
    int middle = find_middle_element(head);

    // Print the middle element
    std::cout << middle << std::endl;

    return 0;
}