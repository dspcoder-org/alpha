// Util.h
#include <iostream>
#include <vector>

// LinkedList class definition
class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Functions declared in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);
void delete_LinkedList(LinkedList* head);

// User-defined function to reverse a linked list
void reverse_Linked_list(LinkedList** head);

// Util.h end

void reverse_Linked_list(LinkedList** head) {
    LinkedList *prev = nullptr, *current = *head, *next = nullptr;

    // Traverse and reverse the linked list
    while (current) {
        next = current->next;  // Store the next node
        current->next = prev;  // Reverse the current node's pointer
        prev = current;        // Move prev to the current node
        current = next;        // Move to the next node
    }

    // Update the head to the new front of the list
    *head = prev;
}