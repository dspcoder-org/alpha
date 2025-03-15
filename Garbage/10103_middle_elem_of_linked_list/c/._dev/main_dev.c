#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question();
extern void print_LinkedList(struct Linked_List* head);

int find_middle_elem(struct Linked_List* head) {
    // Write your code here
    if (head == NULL)
        return -1;
    
    struct Linked_List* slow_ptr = head;
    struct Linked_List* fast_ptr = head;
    
    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }
    
    return slow_ptr->data;
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