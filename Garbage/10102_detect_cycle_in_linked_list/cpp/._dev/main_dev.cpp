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
    LinkedList* slow = head;
    LinkedList* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }

    return false;
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to detect cycle in the linked list
    bool hasCycle = detect_cycle(head);

    // Print the result
    if (hasCycle) {
        std::cout << "true" << std::endl;
    } else {
        std::cout << "false" << std::endl;
    }

    return 0;
}