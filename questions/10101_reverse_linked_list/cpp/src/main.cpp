#include "../inc/util.hpp"
#include <vector>
#include <iostream>

void reverse_Linked_list(LinkedList** head) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to reverse the linked list
    reverse_Linked_list(&head);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}