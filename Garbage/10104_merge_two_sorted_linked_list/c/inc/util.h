#ifndef UTIL_H
#define UTIL_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern void setup_question(struct Linked_List** list1, struct Linked_List** list2);
extern void print_LinkedList(struct Linked_List* head);

#endif // UTIL_H