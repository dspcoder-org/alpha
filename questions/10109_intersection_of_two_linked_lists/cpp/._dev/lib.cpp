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

LinkedList* setup_question(int argc, char* argv[], LinkedList** headB);
void print_Intersection(LinkedList* intersection);

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

// Function to print the intersection node
void print_Intersection(LinkedList* intersection) {
    if (!intersection) {
        std::cout << "null\n";
    } else {
        std::cout << intersection->data << "\n";
    }
}

LinkedList* setup_question(int argc, char* argv[], LinkedList** headB) {

    if (argc == 1) {
        // Input the number of elements for the first list
        int n, m, temp;
        VERIFY((std::cin >> n));

        // Dynamically allocate an array to store the node values for the first list
        int* nodesA = new int[n];

        // Input the values into the array for the first list
        for (int i = 0; i < n; i++) {
            VERIFY((std::cin >> nodesA[i]));
        }

        // Input the number of elements for the second list
        VERIFY((std::cin >> m));

        // Dynamically allocate an array to store the node values for the second list
        int* nodesB = new int[m];

        // Input the values into the array for the second list
        for (int i = 0; i < m; i++) {
            VERIFY((std::cin >> nodesB[i]));
        }

        // Check if there are any extra inputs
        VERIFY((std::cin >> temp).fail() == true);

        // Build the linked lists
        LinkedList* headA = buildLinkedList(nodesA, n);
        *headB = buildLinkedList(nodesB, m);

        return headA;
    }
    else {
        int n = std::stoi(argv[1]);
        int* nodesA = new int[n];
        for (int i = 0; i < n; i++) {
            nodesA[i] = std::stoi(argv[i + 2]);
        }

        int m = std::stoi(argv[n + 2]);
        int* nodesB = new int[m];
        for (int i = 0; i < m; i++) {
            nodesB[i] = std::stoi(argv[n + 3 + i]);
        }

        // Build the linked lists
        LinkedList* headA = buildLinkedList(nodesA, n);
        *headB = buildLinkedList(nodesB, m);

        return headA;
    }
}