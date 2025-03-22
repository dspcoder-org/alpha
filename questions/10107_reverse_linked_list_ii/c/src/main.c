#include "util.h"

void reverse_Linked_list_ii(struct Linked_List** head, int left, int right) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    int left, right;
    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv, &left, &right);
    
    // User function to reverse the linked list between left and right
    reverse_Linked_list_ii(&head, left, right); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}