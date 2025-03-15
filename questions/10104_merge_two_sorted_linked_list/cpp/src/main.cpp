#include "util.hpp"
#include <vector>
#include <iostream>

LinkedList* merge_two_sorted_linked_list(LinkedList* list1, LinkedList* list2) {
    // Write your code here
    return nullptr;
}

int main(int argc, char* argv[]) {
    
    // Setup the linked lists
    LinkedList* list1;
    LinkedList* list2;
    setup_question(argc, argv, &list1, &list2);

    // Call the user function to merge the two sorted linked lists
    LinkedList* merged_list = merge_two_sorted_linked_list(list1, list2);

    // Print the merged linked list
    print_LinkedList(merged_list);

    return 0;
}