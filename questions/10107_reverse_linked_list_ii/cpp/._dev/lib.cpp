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

LinkedList* setup_question(int argc, char* argv[], int* left, int* right);
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

LinkedList* setup_question(int argc, char* argv[], int* left, int* right) {

    if (argc == 1) {
        // Input the number of elements
        int n, temp;
        // Input the number of elements
        VERIFY((std::cin >> n));

        // Dynamically allocate an array to store the node values
        int* nodes = new int[n];

        // Input the values into the array
        for (int i = 0; i < n; i++) {
            VERIFY((std::cin >> nodes[i]));
        }

        // Input left and right
        VERIFY((std::cin >> *left >> *right));

        // Check if there are any extra inputs
        // If there are, then the input is invalid
        VERIFY((std::cin >> temp).fail() == true);

        // Build the linked list
        LinkedList* head = buildLinkedList(nodes, n);

        return head;
    }
    else {
        int n = std::stoi(argv[1]);
        int* nodes = new int[n];
        for (int i = 0; i < n; i++) {
            nodes[i] = std::stoi(argv[i + 2]);
        }

        *left = std::stoi(argv[n + 2]);
        *right = std::stoi(argv[n + 3]);

        LinkedList* head = buildLinkedList(nodes, n);

        return head;
    }
}