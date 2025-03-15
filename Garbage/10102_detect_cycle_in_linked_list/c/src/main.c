#include "../inc/util.h"

bool detect_cycle(struct Linked_List* head) {
    // Write your code here
    
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to detect cycle in the linked list
    bool hasCycle = detect_cycle(head);

    // Print the result
    if (hasCycle) {
        printf("true\n");
    } else {
        printf("false\n");
    }
    
    return 0;
}