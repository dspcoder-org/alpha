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

struct Linked_List* mergeTwoLists(struct Linked_List* l1, struct Linked_List* l2){
    // give me solution below
    struct Linked_List* head = NULL;
    struct Linked_List* tail = NULL;
    struct Linked_List* temp = NULL;    

    while(l1 != NULL && l2 != NULL){
        if(l1->data < l2->data){
            temp = l1;
            l1 = l1->next;
        }else{
            temp = l2;
            l2 = l2->next;
        }
        temp->next = NULL;
        if(head == NULL){
            head = temp;
            tail = temp;
        }else{
            tail->next = temp;
            tail = temp;
        }
    }

    if(l1 != NULL){
        if(head == NULL){
            head = l1;
        }else{
            tail->next = l1;
        }
    }

    if(l2 != NULL){
        if(head == NULL){
            head = l2;
        }else{
            tail->next = l2;
        }
    }

    return head;

}

int main(){

    struct Linked_List *list1, *list2;

    // Setup the linked list
    setup_question(&list1, &list2);

    // User function to merge the linked lists
    struct Linked_List* head = mergeTwoLists(list1, list2);
    
    // Print the linked list
    print_LinkedList(head);
    
    return 0;
}