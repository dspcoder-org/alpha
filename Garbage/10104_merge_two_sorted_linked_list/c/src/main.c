#include "util.h"

struct Linked_List* merge_two_sorted_linked_list(struct Linked_List* list1, struct Linked_List* list2) {
    // Write your code here
    return NULL;
}

int main(int argc, char* argv[]) {

    // Setup the linked lists
    struct Linked_List* list1;
    struct Linked_List* list2;
    setup_question(argc, argv, &list1, &list2);
    
    // User function to merge the two sorted linked lists
    struct Linked_List* merged_list = merge_two_sorted_linked_list(list1, list2); 

    // Print the merged linked list
    print_LinkedList(merged_list);
    
    return 0;
}