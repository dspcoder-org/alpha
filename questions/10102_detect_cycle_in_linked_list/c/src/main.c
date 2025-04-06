#include "util.h"

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle_in_linked_list(head); 

    // Print the result
    printf("%s\n", has_cycle ? "true" : "false");

    // Free the linked list to prevent memory leaks
    free_LinkedList(head);
    
    return 0;
}