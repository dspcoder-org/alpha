#include "util.hpp"
#include <vector>
#include <iostream>

LinkedList* getIntersectionNode(LinkedList* headA, LinkedList* headB) {
    // Write your code here
    return nullptr;
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