#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question(int argc, char* argv[], int* left, int* right);
extern void print_LinkedList(struct Linked_List* head);

void reverse_Linked_list_ii(struct Linked_List** head, int left, int right) {
    if (left == right) return;

    struct Linked_List dummy;
    dummy.next = *head;
    struct Linked_List* prev = &dummy;

    for (int i = 1; i < left; ++i) {
        prev = prev->next;
    }

    struct Linked_List* const reverse_start = prev;
    prev = reverse_start->next;
    struct Linked_List* curr = prev->next;

    for (int i = left; i < right; ++i) {
        prev->next = curr->next;
        curr->next = reverse_start->next;
        reverse_start->next = curr;
        curr = prev->next;
    }

    *head = dummy.next;
}

int main(int argc, char* argv[]) {

    int left, right;
    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv, &left, &right);
    
    // User function to reverse the linked list between left and right
    reverse_Linked_list_ii(&head, left, right); 

    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}