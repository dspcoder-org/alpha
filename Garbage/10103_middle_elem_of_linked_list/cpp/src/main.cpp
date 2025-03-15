#include "../inc/util.hpp"
#include <vector>
#include <iostream>

int find_middle_elem(LinkedList* head) {
    // Write your code here
    
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to find the middle element of the linked list
    int middle_elem = find_middle_elem(head);

    // Print the middle element
    std::cout << middle_elem << std::endl;

    return 0;
}