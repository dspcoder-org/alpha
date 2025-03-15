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
    if (head == nullptr || head->next == nullptr) {
        return false;
    }

    LinkedList* slow = head;
    LinkedList* fast = head->next;

    while (slow != fast) {
        if (fast == nullptr || fast->next == nullptr) {
            return false;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
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