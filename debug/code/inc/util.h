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
extern struct Linked_List* setup_question(int argc, char* argv[], struct Linked_List** headB);
extern void print_Intersection(struct Linked_List* intersection);

#endif // UTIL_H