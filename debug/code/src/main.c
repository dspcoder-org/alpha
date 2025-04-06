
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question(int argc, char* argv[], struct Linked_List** headB);
extern void print_Intersection(struct Linked_List* intersection);

struct Linked_List* getIntersectionNode(struct Linked_List* headA, struct Linked_List* headB) {
    if (!headA || !headB) return NULL;

    struct Linked_List* a = headA;
    struct Linked_List* b = headB;

    while (a != b) {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }

    return a;
}

int main(int argc, char* argv[]) {

    // Setup the linked lists
    struct Linked_List* headB;
    struct Linked_List* headA = setup_question(argc, argv, &headB);
    
    // User function to find the intersection node
    struct Linked_List* intersection = getIntersectionNode(headA, headB); 

    // Print the intersection node
    print_Intersection(intersection);
    
    return 0;
}