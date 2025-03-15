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
    if (head == NULL || head->next == NULL) {
        return false;
    }

    struct Linked_List* slow = head;
    struct Linked_List* fast = head->next;

    while (slow != fast) {
        if (fast == NULL || fast->next == NULL) {
            return false;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head); 

    // Print the result
    printf("%s\n", has_cycle ? "true" : "false");
    
    return 0;
}