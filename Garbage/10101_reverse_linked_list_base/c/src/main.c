#include "util.h"

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to reverse the linked list
    reverse_Linked_list(&head); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}