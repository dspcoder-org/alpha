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

LinkedList* setup_question();
void print_LinkedList(LinkedList* head);



// Function to build a linked list from an array
LinkedList* buildLinkedList(int arr[], int n, int pos) {
    if (n == 0) {
        return nullptr;
    }

    LinkedList* head = new LinkedList(arr[0]);
    LinkedList* dummy_head = head;

    for (int i = 1; i < n; ++i) {
        dummy_head->next = new LinkedList(arr[i]);
        dummy_head = dummy_head->next;
    }

    // Create cycle if pos is valid
    if (pos >= 0 && pos < n) {
        LinkedList* cycleNode = head;
        for (int i = 0; i < pos; i++) {
            cycleNode = cycleNode->next;
        }
        dummy_head->next = cycleNode;
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

LinkedList* setup_question() {
    
    // Input the number of elements and position of cycle
    int n, pos, temp;
    VERIFY((std::cin >> n >> pos));

    // Dynamically allocate an array to store the node values
    int* nodes = new int[n];

    // Input the values into the array
    for (int i = 0; i < n; i++) {
        VERIFY((std::cin >> nodes[i]));
    }
    // Check if there are any extra inputs
    // If there are, then the input is invalid
    VERIFY((std::cin >> temp).fail() == true);

    // Build the linked list with cycle
    LinkedList* head = buildLinkedList(nodes, n, pos);

    return head;
}