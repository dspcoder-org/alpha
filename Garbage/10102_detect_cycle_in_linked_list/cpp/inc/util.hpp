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

// Function declarations

LinkedList* setup_question(int argc, char* argv[]);
void print_LinkedList(LinkedList* head);

#endif // UTIL_H