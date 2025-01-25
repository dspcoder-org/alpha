#include "../inc/util.h"

void reverse_Linked_list(struct Linked_List** head) {
    // Write your code here
    
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to reverse the linked list
    reverse_Linked_list(&head); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}