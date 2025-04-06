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
void delete_LinkedList(LinkedList* head);

// User function
void reverse_Linked_list(LinkedList** head);

// Util.h end


int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to reverse the linked list
    reverse_Linked_list(&head);

    // Print the linked list
    print_LinkedList(head);

    // Free the memory allocated for the linked list
    delete_LinkedList(head);

    return 0;
}