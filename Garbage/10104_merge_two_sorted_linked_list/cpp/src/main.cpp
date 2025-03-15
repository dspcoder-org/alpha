#include "../inc/util.hpp"
#include <vector>
#include <iostream>

// Function to merge two sorted linked lists
LinkedList* mergeTwoLists(LinkedList* l1, LinkedList* l2) {
    // Write your code here

    return NULL;
}

int main() {
    
    LinkedList *list1, *list2;

    // Setup the linked list
    setup_question(&list1, &list2);

    // User function to merge the linked lists
    LinkedList* head = mergeTwoLists(list1, list2);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}