#include "../inc/util.h"

struct Linked_List* mergeTwoLists(struct Linked_List* l1, struct Linked_List* l2){
    // Write your code here

    return NULL;
}

int main(){

    struct Linked_List *list1, *list2;

    // Setup the linked list
    setup_question(&list1, &list2);

    // User function to merge the linked lists
    struct Linked_List* head = mergeTwoLists(list1, list2);
    
    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}