// util.h
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function declred in libdspcoder.a
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);

// User function
extern void reverse_Linked_list(struct Linked_List** head);

// util.h end

void reverse_Linked_list(struct Linked_List** head) {
    struct Linked_List* prev = NULL;
    struct Linked_List* current = *head;
    struct Linked_List* next = NULL;

    while (current != NULL) {
        // Store the next node
        next = current->next;
        // Reverse the current node's pointer
        current->next = prev;
        // Move pointers one position ahead
        prev = current;
        current = next;
    }
    *head = prev; // Update the head to the new first element
}