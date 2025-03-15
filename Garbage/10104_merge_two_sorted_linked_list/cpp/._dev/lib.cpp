#include <iostream>
#include <vector>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        std::cout << "._bad_input\n"; \
        exit(0);               \
    }

// Copy content of util.hpp
class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

void setup_question(LinkedList** list1, LinkedList** list2);
void print_LinkedList(LinkedList* head);

// Function to build a linked list from an array
LinkedList* buildLinkedList(int arr[], int n) {
    if (n == 0) {
        return nullptr;
    }

    LinkedList* head = new LinkedList(arr[0]);
    LinkedList* dummy_head = head;

    for (int i = 1; i < n; ++i) {
        dummy_head->next = new LinkedList(arr[i]);
        dummy_head = dummy_head->next;
    }

    return head;
}

// Function to print the linked list
void print_LinkedList(LinkedList* head) {
    if (!head) {
        return;
    }

    while (head) {
        std::cout << head->data;
        if (head->next) {
            std::cout << " ";
        }
        head = head->next;
    }
    std::cout << std::endl;
}

// # Takes two linked list as input
void setup_question(LinkedList** list1, LinkedList** list2) {
    
    // Input the number of elements for the first list
    int n1, n2, temp;
    VERIFY((std::cin >> n1));

    // Dynamically allocate an array to store the node values for the first list
    int* nodes1 = new int[n1];

    // Input the values into the array for the first list
    for (int i = 0; i < n1; i++) {
        VERIFY((std::cin >> nodes1[i]));
    }

    // Input the number of elements for the second list
    VERIFY((std::cin >> n2));

    // Dynamically allocate an array to store the node values for the second list
    int* nodes2 = new int[n2];

    // Input the values into the array for the second list
    for (int i = 0; i < n2; i++) {
        VERIFY((std::cin >> nodes2[i]));
    }

    // Check if there are any extra inputs
    VERIFY((std::cin >> temp).fail() == true);

    // Build the linked lists
    *list1 = buildLinkedList(nodes1, n1);
    *list2 = buildLinkedList(nodes2, n2);

}