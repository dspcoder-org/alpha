#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question();
extern void print_LinkedList(struct Linked_List* head);

void pair_sum_count(struct Linked_List* head, int target) {
    // Implement the pair sum count algorithm
    struct Linked_List* current = head;
    int count = 0;
    bool visited[2001] = {false}; // To track visited elements, considering range -1000 to 1000

    while (current != NULL) {
        int complement = target - current->data;
        if (complement >= -1000 && complement <= 1000 && visited[complement + 1000]) {
            count++;
            visited[complement + 1000] = false; // Ensure each pair is counted only once
        } else {
            visited[current->data + 1000] = true;
        }
        current = current->next;
    }

    printf("%d\n", count);
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