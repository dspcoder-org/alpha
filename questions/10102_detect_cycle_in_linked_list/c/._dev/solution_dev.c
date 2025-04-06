// util.h start
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Functions declared in libdspcoder.a
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);
extern void free_LinkedList(struct Linked_List* head);

// User functions
extern bool detect_cycle_in_linked_list(struct Linked_List* head);

// util.h end

// Function to detect a cycle in a linked list
bool detect_cycle_in_linked_list(struct Linked_List* head) {
    struct Linked_List* slow = head;
    struct Linked_List* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true; // Cycle detected
        }
    }
    return false; // No cycle
}