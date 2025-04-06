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

LinkedList* remove_duplicates(LinkedList* head) {
    LinkedList* current = head;
    while (current != nullptr && current->next != nullptr) {
        if (current->data == current->next->data) {
            LinkedList* next_next = current->next->next;
            delete current->next;
            current->next = next_next;
        } else {
            current = current->next;
        }
    }
    return head;
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to remove duplicates from the linked list
    head = remove_duplicates(head);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}