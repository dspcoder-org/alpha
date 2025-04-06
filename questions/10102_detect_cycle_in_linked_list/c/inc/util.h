#ifndef UTIL_H
#define UTIL_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Functions declared in libdspcoder.a
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);
extern void free_LinkedList(struct Linked_List* head);

// User functions
extern bool detect_cycle_in_linked_list(struct Linked_List* head);

#endif // UTIL_H