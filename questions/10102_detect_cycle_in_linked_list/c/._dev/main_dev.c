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
extern bool detect_cycle_in_linked_list(struct Linked_List* head);

int main(int argc, char* argv[]) {
    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle_in_linked_list(head); 

    // Print the result
    printf("%s\n", has_cycle ? "true" : "false");

    // Free the linked list to prevent memory leaks
    free_LinkedList(head);
    
    return 0;
}