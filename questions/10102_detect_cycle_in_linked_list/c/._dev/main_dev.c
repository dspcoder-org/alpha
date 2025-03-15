#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);

bool detect_cycle(struct Linked_List* head) {
    struct Linked_List* slow = head;
    struct Linked_List* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }
    return false;
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