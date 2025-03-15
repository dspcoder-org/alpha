#include "../inc/util.h"

void pair_sum_count(struct Linked_List* head, int target) {
    // Leave this function blank for user to write
}

int main() {
    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to count pairs
    int target;
    scanf("%d", &target);
    pair_sum_count(head, target);

    return 0;
}