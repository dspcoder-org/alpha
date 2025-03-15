#include "../inc/util.h"

int find_middle_elem(struct Linked_List* head) {
    // Write your code here
    
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to find the middle element of the linked list
    int middle_elem = find_middle_elem(head); 

    // Print the middle element
    printf("%d\n", middle_elem);
    
    return 0;
}