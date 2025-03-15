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

bool isPalindrome(struct Linked_List* head) {
    // Write your code here
    if (!head || !head->next) return true;

    struct Linked_List* slow = head;
    struct Linked_List* fast = head;
    struct Linked_List* prev = NULL;
    struct Linked_List* temp;

    // Find the middle of the linked list
    while (fast && fast->next) {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast) {
        slow = slow->next;
    }

    // Compare the two halves
    while (slow) {
        if (slow->data != prev->data) return false;
        slow = slow->next;
        prev = prev->next;
    }

    return true;
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to check if the linked list is a palindrome
    bool result = isPalindrome(head); 

    // Print the result
    printf(result ? "true\n" : "false\n");
    
    return 0;
}