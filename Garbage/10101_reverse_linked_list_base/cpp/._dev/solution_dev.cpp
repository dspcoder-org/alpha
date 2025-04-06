// Util.h
#include <iostream>
#include <vector>

class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declred in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);

// User function
void reverse_Linked_list(LinkedList** head);

// Util.h end

void reverse_Linked_list(LinkedList** head) {
    LinkedList* prev = nullptr;
    LinkedList* current = *head;
    LinkedList* next = nullptr;

    while (current != nullptr) {
        // Store the next node
        next = current->next;
        // Reverse the current node's pointer
        current->next = prev;
        // Move pointers one position ahead
        prev = current;
        current = next;
    }

    // Update the head to the new front of the list
    *head = prev;
}