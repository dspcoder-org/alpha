#include <vector>
#include <iostream>


class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

LinkedList* setup_question();
void print_LinkedList(LinkedList* head);

bool detect_cycle(LinkedList* head) {
    // Write your code here
    LinkedList* slow = head;  // Slow pointer
    LinkedList* fast = head;  // Fast pointer

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;  // Cycle detected
        }
    }

    return false;  // No cycle found
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to detect cycle in the linked list
    bool has_cycle = detect_cycle(head);

    // Print the result
    std::cout << (has_cycle ? "true" : "false") << std::endl;

    return 0;
}