#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

void setup_question(int argc, char* argv[], LinkedList** list1, LinkedList** list2);
void print_LinkedList(LinkedList* head);

LinkedList* merge_two_sorted_linked_list(LinkedList* list1, LinkedList* list2) {
    LinkedList dummy(0);
    LinkedList* tail = &dummy;

    while (list1 && list2) {
        if (list1->data < list2->data) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }
    tail->next = list1 ? list1 : list2;
    return dummy.next;
}

int main(int argc, char* argv[]) {
    
    // Setup the linked lists
    LinkedList* list1;
    LinkedList* list2;
    setup_question(argc, argv, &list1, &list2);

    // Call the user function to merge the two sorted linked lists
    LinkedList* merged_list = merge_two_sorted_linked_list(list1, list2);

    // Print the merged linked list
    print_LinkedList(merged_list);

    return 0;
}