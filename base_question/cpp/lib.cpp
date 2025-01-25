#include <iostream>
#include <vector>

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

LinkedList* setup_question() {
    
    // Input the number of elements
    int n;
    // Input the number of elements
    std::cin >> n;

    // Dynamically allocate an array to store the node values
    int* nodes = new int[n];

    // Input the values into the array
    for (int i = 0; i < n; i++) {
        std::cin >> nodes[i];
    }

    // Build the linked list
    LinkedList* head = buildLinkedList(nodes, n);

    return head;
}