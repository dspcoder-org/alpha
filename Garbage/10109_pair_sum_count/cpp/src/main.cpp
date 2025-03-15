#include "../inc/util.hpp"
#include <vector>
#include <iostream>

void pair_sum_count(LinkedList* head, int target) {
    // Leave this function blank for user to write
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