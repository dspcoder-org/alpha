#include <vector>
#include <iostream>

class LinkedList {
public:
    int data;
    LinkedList* next;

    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declarations

LinkedList* setup_question(int argc, char* argv[], LinkedList** headB);
void print_Intersection(LinkedList* intersection);

LinkedList* getIntersectionNode(LinkedList* headA, LinkedList* headB) {
    if (!headA || !headB) return nullptr;

    LinkedList* a = headA;
    LinkedList* b = headB;

    while (a != b) {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }

    return a;
}

int main(int argc, char* argv[]) {
    
    // Setup the linked lists
    LinkedList* headB;
    LinkedList* headA = setup_question(argc, argv, &headB);

    // Call the user function to find the intersection node
    LinkedList* intersection = getIntersectionNode(headA, headB);

    // Print the intersection node
    print_Intersection(intersection);

    return 0;
}