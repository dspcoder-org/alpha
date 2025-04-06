#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern void setup_question(int argc, char* argv[], struct Linked_List** list1, struct Linked_List** list2);
extern void print_LinkedList(struct Linked_List* head);

struct Linked_List* merge_two_sorted_linked_list(struct Linked_List* list1, struct Linked_List* list2) {
    struct Linked_List dummy;
    struct Linked_List* tail = &dummy;
    dummy.next = NULL;

    while (list1 && list2) {
        if (list1->data < list2->data) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }
    tail->next = list1 ? list1 : list2;
    return dummy.next;
}

int main(int argc, char* argv[]) {

    // Setup the linked lists
    struct Linked_List* list1;
    struct Linked_List* list2;
    setup_question(argc, argv, &list1, &list2);
    
    // User function to merge the two sorted linked lists
    struct Linked_List* merged_list = merge_two_sorted_linked_list(list1, list2); 

    // Print the merged linked list
    print_LinkedList(merged_list);
    
    return 0;
}