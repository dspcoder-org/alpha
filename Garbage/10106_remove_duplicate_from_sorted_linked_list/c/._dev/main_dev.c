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

struct Linked_List* remove_duplicates(struct Linked_List* head) {
    struct Linked_List* current = head;
    while (current != NULL && current->next != NULL) {
        if (current->data == current->next->data) {
            struct Linked_List* next_next = current->next->next;
            free(current->next);
            current->next = next_next;
        } else {
            current = current->next;
        }
    }
    return head;
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to remove duplicates from the linked list
    head = remove_duplicates(head); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}