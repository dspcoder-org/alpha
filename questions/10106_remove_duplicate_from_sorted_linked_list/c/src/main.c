#include "util.h"

struct Linked_List* remove_duplicates(struct Linked_List* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to remove duplicates from the linked list
    head = remove_duplicates(head); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}