#include "util.h"

struct Linked_List* getIntersectionNode(struct Linked_List* headA, struct Linked_List* headB) {
    // Write your code here
    return NULL;
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