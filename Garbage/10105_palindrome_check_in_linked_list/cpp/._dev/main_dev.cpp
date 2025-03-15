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

bool isPalindrome(LinkedList* head) {
    // Write your code here
    if (!head || !head->next) return true;

    LinkedList* slow = head;
    LinkedList* fast = head;
    LinkedList* prev = nullptr;
    LinkedList* temp;

    // Find the middle of the linked list
    while (fast && fast->next) {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast) {
        slow = slow->next;
    }

    // Compare the two halves
    while (slow) {
        if (slow->data != prev->data) return false;
        slow = slow->next;
        prev = prev->next;
    }

    return true;
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to check if the linked list is a palindrome
    bool result = isPalindrome(head);

    // Print the result
    std::cout << (result ? "true" : "false") << std::endl;

    return 0;
}