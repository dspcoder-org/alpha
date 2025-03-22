#include "util.hpp"
#include <vector>
#include <iostream>

void reverse_Linked_list_ii(LinkedList** head, int left, int right) {
    // Write your code here
}

int main(int argc, char* argv[]) {
    
    int left, right;
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv, &left, &right);

    // Call the user function to reverse the linked list between left and right
    reverse_Linked_list_ii(&head, left, right);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}