// Util.h
#include <iostream>
#include <vector>

// LinkedList class definition
class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Functions declared in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);
void delete_LinkedList(LinkedList* head);

// User-defined function to detect a cycle in a linked list
bool detect_cycle_in_linked_list(LinkedList* head);

// Util.h end

bool detect_cycle_in_linked_list(LinkedList* head) {
    LinkedList* slow = head;
    LinkedList* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true; // Cycle detected
        }
    }
    return false; // No cycle
}