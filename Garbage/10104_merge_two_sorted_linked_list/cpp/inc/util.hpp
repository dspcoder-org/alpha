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

void setup_question(LinkedList** list1, LinkedList** list2);
void print_LinkedList(LinkedList* head);

#endif // UTIL_H