#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <vector>

class LinkedList {
public:
    int data;
    LinkedList* next;
    LinkedList(int val) : data(val), next(nullptr) {}
};

// Function declred in libdspcoder.a
LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);

// User function
void reverse_Linked_list(LinkedList** head);

#endif // UTIL_H