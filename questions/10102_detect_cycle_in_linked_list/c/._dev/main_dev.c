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

bool detect_cycle(struct Linked_List* head) {
    // Write your code here
    struct Linked_List* slow = head;  // Slow pointer
    struct Linked_List* fast = head;  // Fast pointer

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;  // Cycle detected
        }
    }

    return false;  // No cycle found
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head); 

    // Print the result
    printf(has_cycle ? "true\n" : "false\n");
    
    return 0;
}