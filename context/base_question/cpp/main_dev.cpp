#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);

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

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to reverse the linked list
    reverse_Linked_list(&head);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}