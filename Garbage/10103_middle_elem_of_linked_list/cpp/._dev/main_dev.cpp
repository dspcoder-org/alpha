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

int find_middle_elem(LinkedList* head) {
    // Write your code here
    if (head == nullptr)
        return -1;
    
    LinkedList* slow_ptr = head;
    LinkedList* fast_ptr = head;
    
    while (fast_ptr != nullptr && fast_ptr->next != nullptr) {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }
    
    return slow_ptr->data;
}

int main() {
    
    // Setup the linked list
    LinkedList* head = setup_question();

    // Call the user function to find the middle element of the linked list
    int middle_elem = find_middle_elem(head);

    // Print the middle element
    std::cout << middle_elem << std::endl;

    return 0;
}