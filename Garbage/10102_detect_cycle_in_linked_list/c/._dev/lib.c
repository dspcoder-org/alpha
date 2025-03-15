#include <stdio.h>
#include <stdlib.h>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        printf("._bad_input"); \
        exit(0);               \
    }                            \

// Content of util.h

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question();
extern void print_LinkedList(struct Linked_List* head);

// end of util.h

struct Linked_List* buildLinkedList(int arr[], int n, int pos){
    
    struct Linked_List* head = (struct Linked_List* ) malloc(sizeof(struct Linked_List));

    if(n == 0){
        return NULL; 
    }

    struct Linked_List* dummy_head = head; 
    
    for(int i = 0; i < n ; i++){
        dummy_head->data = arr[i]; 
        if (i != n-1){
            dummy_head->next = (struct Linked_List* ) malloc(sizeof(struct Linked_List));
            dummy_head = dummy_head->next; 
        }
    }

    // Create cycle if pos is valid
    if (pos >= 0 && pos < n) {
        struct Linked_List* cycleNode = head;
        for (int i = 0; i < pos; i++) {
            cycleNode = cycleNode->next;
        }
        dummy_head->next = cycleNode;
    }

    return head; 
}

void print_LinkedList(struct Linked_List* head){

    if(head == NULL){
        printf(""); 
    }

    while(head){
        printf("%d", head->data); 
        if(head->next){    
            printf(" "); 
        }
        head = head->next;
    }
    printf("\n"); 
}

struct Linked_List* setup_question(){
    int n, pos, temp;
    
    // Input the number of elements and position of cycle
    VERIFY(((scanf("%d", &n)) > 0)); 
    VERIFY(((scanf("%d", &pos)) > 0));

    // Create an array to store the node values
    int nodes[n];

    // Input the values into the array
    for (int i = 0; i < n; i++) {
        VERIFY(((scanf("%d", &nodes[i])) > 0));
    }

    VERIFY(((scanf("%d", &temp)) == EOF));

    // Build the linked list with cycle
    struct Linked_List* head =  buildLinkedList(nodes, n, pos); 

    return head;
}