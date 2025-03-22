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

bool is_palindrome(struct Linked_List* head) {
    if (!head || !head->next) return true;

    struct Linked_List* slow = head;
    struct Linked_List* fast = head;
    struct Linked_List* prev = NULL;
    struct Linked_List* temp;

    // Find the middle of the linked list
    while (fast && fast->next) {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast) {
        slow = slow->next;
    }

    // Compare the two halves
    while (prev && slow) {
        if (prev->data != slow->data) {
            return false;
        }
        prev = prev->next;
        slow = slow->next;
    }

    return true;
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to check if the linked list is a palindrome
    bool result = is_palindrome(head); 

    // Print the result
    printf(result ? "true\n" : "false\n");
    
    return 0;
}