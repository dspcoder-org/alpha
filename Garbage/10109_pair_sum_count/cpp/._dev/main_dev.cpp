#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations
LinkedList* setup_question();
void print_LinkedList(LinkedList* head);

void pair_sum_count(LinkedList* head, int target) {
    // Implement the pair sum count algorithm
    LinkedList* current = head;
    int count = 0;
    bool visited[2001] = {false}; // To track visited elements, considering range -1000 to 1000

    while (current != nullptr) {
        int complement = target - current->data;
        if (complement >= -1000 && complement <= 1000 && visited[complement + 1000]) {
            count++;
            visited[complement + 1000] = false; // Ensure each pair is counted only once
        } else {
            visited[current->data + 1000] = true;
        }
        current = current->next;
    }

    std::cout << count << std::endl;
}

int main() {
    // Setup the linked list
    LinkedList* head = setup_question();

    // User function to count pairs
    int target;
    std::cin >> target;
    pair_sum_count(head, target);

    return 0;
}