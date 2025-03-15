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

void reverse_Linked_list(struct Linked_List** head) {
    struct Linked_List* prev = NULL;           // Previous node
    struct Linked_List* current = *head;       // Current node
    struct Linked_List* next = NULL;            // Next node

    while (current != NULL) {
        next = current->next;                   // Store the next node
        current->next = prev;                   // Reverse the current node's pointer
        prev = current;                         // Move prev and current one step forward
        current = next;
    }
    *head = prev; 
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