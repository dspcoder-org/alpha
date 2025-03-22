#include "util.hpp"
#include <vector>
#include <iostream>

LinkedList* remove_duplicates(LinkedList* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to remove duplicates from the linked list
    head = remove_duplicates(head);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}