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

bool is_palindrome(LinkedList* head) {
    if (!head || !head->next) return true;

    LinkedList* slow = head;
    LinkedList* fast = head;
    LinkedList* prev = nullptr;
    LinkedList* temp;

    // Find the middle of the linked list
    while (fast && fast->next) {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast) {
        slow = slow->next;
    }

    // Compare the two halves
    while (prev && slow) {
        if (prev->data != slow->data) {
            return false;
        }
        prev = prev->next;
        slow = slow->next;
    }

    return true;
}

int main(int argc, char* argv[]) {
    
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv);

    // Call the user function to check if the linked list is a palindrome
    bool result = is_palindrome(head);

    // Print the result
    std::cout << (result ? "true" : "false") << std::endl;

    return 0;
}