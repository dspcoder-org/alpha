#include <iostream>
#include <vector>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        std::cout << "._bad_input\n"; \
        exit(0);               \
    }

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations
LinkedList* setup_question();
void print_LinkedList(LinkedList* head);

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
    int n, target;
    VERIFY((std::cin >> n));

    int* nodes = new int[n];

    for (int i = 0; i < n; i++) {
        VERIFY((std::cin >> nodes[i]));
    }

    VERIFY((std::cin >> target));

    LinkedList* head = buildLinkedList(nodes, n);

    return head;
}