#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

void setup_question(LinkedList** list1, LinkedList** list2);
void print_LinkedList(LinkedList* head);

LinkedList* mergeTwoLists(LinkedList* l1, LinkedList* l2) {
    LinkedList dummy(0);
    LinkedList* tail = &dummy;

    while (l1 && l2) {
        if (l1->data < l2->data) {
            tail->next = l1;
            l1 = l1->next;
        } else {
            tail->next = l2;
            l2 = l2->next;
        }
        tail = tail->next;
    }
    tail->next = l1 ? l1 : l2;
    return dummy.next;
}

int main() {
    
    LinkedList *list1, *list2;

    // Setup the linked list
    setup_question(&list1, &list2);

    // User function to merge the linked lists
    LinkedList* head = mergeTwoLists(list1, list2);

    // Print the linked list
    print_LinkedList(head);

    return 0;
}