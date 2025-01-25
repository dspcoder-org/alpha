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
    struct Linked_List* slow_ptr = head;
    struct Linked_List* fast_ptr = head;

    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
        if (slow_ptr == fast_ptr) {
            return true;
        }
    }

    return false;
}

int main() {
    // Setup the linked list
    struct Linked_List* head = setup_question();

    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head);

    // Print the result
    printf("%s\n", has_cycle ? "true" : "false");

    return 0;
}