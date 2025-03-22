#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

LinkedList* setup_question(int argc, char* argv[], int* left, int* right);
void print_LinkedList(LinkedList* head);

void reverse_Linked_list_ii(LinkedList** head, int left, int right) {
    if (left == right) return;

    LinkedList dummy(0);
    dummy.next = *head;
    LinkedList* prev = &dummy;

    for (int i = 1; i < left; ++i) {
        prev = prev->next;
    }

    LinkedList* const reverse_start = prev;
    prev = reverse_start->next;
    LinkedList* curr = prev->next;

    for (int i = left; i < right; ++i) {
        prev->next = curr->next;
        curr->next = reverse_start->next;
        reverse_start->next = curr;
        curr = prev->next;
    }

    *head = dummy.next;
}

int main(int argc, char* argv[]) {
    
    int left, right;
    // Setup the linked list
    LinkedList* head = setup_question(argc, argv, &left, &right);

    // Call the user function to reverse the linked list between left and right
    reverse_Linked_list_ii(&head, left, right);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}