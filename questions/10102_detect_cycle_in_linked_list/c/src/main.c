#include "util.h"

bool detect_cycle(struct Linked_List* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head); 

    // Print the result
    printf("%s\n", has_cycle ? "true" : "false");
    
    return 0;
}