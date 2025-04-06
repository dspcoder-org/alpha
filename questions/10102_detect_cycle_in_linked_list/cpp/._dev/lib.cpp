#include <iostream>
#include <vector>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        std::cout << "._bad_input\n"; \
        exit(0);               \
    }

// Util.h
#include <iostream>
#include <vector>

class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declared in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);

// User function
bool detect_cycle_in_linked_list(LinkedList* head);

// Util.h end

// Function to build a linked list from an array
LinkedList* buildLinkedList(int arr[], int n, int pos) {
    if (n == 0) {
        return nullptr;
    }

    LinkedList* head = new LinkedList(arr[0]);
    LinkedList* dummy_head = head;
    LinkedList* cycle_node = nullptr;

    for (int i = 1; i < n; ++i) {
        dummy_head->next = new LinkedList(arr[i]);
        dummy_head = dummy_head->next;
        if (i == pos) {
            cycle_node = dummy_head;
        }
    }

    if (pos != -1) {
        dummy_head->next = cycle_node; // Create cycle if pos is not -1
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

// Function to delete the linked list
void delete_LinkedList(LinkedList* head) {
    while (head) {
        LinkedList* temp = head;
        head = head->next;
        delete temp;
    }
}

LinkedList* setup_question(int argc, char* argv[]) {

    if (argc == 1) {
        // Input the number of elements and position
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

        // Build the linked list
        LinkedList* head = buildLinkedList(nodes, n, pos);
        delete[] nodes; // Free allocated memory

        return head;
    }
    else {
        int n = std::stoi(argv[1]);
        int pos = std::stoi(argv[2]);
        int* nodes = new int[n];
        for (int i = 0; i < n; i++) {
            nodes[i] = std::stoi(argv[i + 3]);
        }
        LinkedList* head = buildLinkedList(nodes, n, pos);
        delete[] nodes; // Free allocated memory

        return head;
    }
}