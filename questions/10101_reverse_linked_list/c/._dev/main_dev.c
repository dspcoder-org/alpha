// util.h
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function declared in libdspcoder.a
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);
extern void free_LinkedList(struct Linked_List* head);

// User function
extern void reverse_Linked_list(struct Linked_List** head);

int main(int argc, char* argv[]) {
    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to reverse the linked list
    reverse_Linked_list(&head); 

    // Print the linked list
    print_LinkedList(head);

    // Free the linked list to prevent memory leaks
    free_LinkedList(head);
    
    return 0;
}