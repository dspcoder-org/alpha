#include "util.h"

int find_middle_element(struct Linked_List* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to find the middle element
    int middle = find_middle_element(head); 

    // Print the middle element
    printf("%d\n", middle);
    
    return 0;
}