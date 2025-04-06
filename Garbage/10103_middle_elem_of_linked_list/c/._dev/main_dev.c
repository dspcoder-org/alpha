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

int find_middle_element(struct Linked_List* head) {
    struct Linked_List* slow = head;
    struct Linked_List* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow->data;
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to find the middle element
    int middle = find_middle_element(head); 

    // Print the middle element
    printf("%d\n", middle);
    
    return 0;
}