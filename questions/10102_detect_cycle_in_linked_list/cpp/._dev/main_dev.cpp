// Util.h
#include <iostream>
#include <vector>

class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declared in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);
void delete_LinkedList(LinkedList* head);

// User function
bool detect_cycle_in_linked_list(LinkedList* head);

// Util.h end


int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to detect cycle in the linked list
    bool has_cycle = detect_cycle_in_linked_list(head);

    // Print the result
    std::cout << (has_cycle ? "true" : "false") << std::endl;

    // Free the memory allocated for the linked list
    delete_LinkedList(head);

    return 0;
}