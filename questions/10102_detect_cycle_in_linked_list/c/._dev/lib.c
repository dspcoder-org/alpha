#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        printf("._bad_input"); \
        exit(0);               \
    }

// Content of util.h

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Linked_List {
    int data;
    struct Linked_List* next;
};

// Function prototypes
extern struct Linked_List* setup_question(int argc, char* argv[]);
extern void print_LinkedList(struct Linked_List* head);

// end of util.h

struct Linked_List* buildLinkedList(int arr[], int n, int pos){
    
    struct Linked_List* head = (struct Linked_List* ) malloc(sizeof(struct Linked_List));

    if(n == 0){
        return NULL; 
    }

    struct Linked_List* dummy_head = head; 
    struct Linked_List* cycle_node = NULL;
    
    for(int i = 0; i < n ; i++){
        dummy_head->data = arr[i]; 
        if (i == pos) {
            cycle_node = dummy_head;
        }
        if (i != n-1){
            dummy_head->next = (struct Linked_List* ) malloc(sizeof(struct Linked_List));
            dummy_head = dummy_head->next; 
        }
    }

    if (pos != -1) {
        dummy_head->next = cycle_node;
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

struct Linked_List* setup_question(int argc, char* argv[]) {

    if (argc == 1) {
        int n, pos, temp;
        
        // Input the number of elements and position
        VERIFY(((scanf("%d %d", &n, &pos)) > 0));

        // Create an array to store the node values
        int nodes[n];

        // Input the values into the array
        for (int i = 0; i < n; i++) {
            VERIFY(((scanf("%d", &nodes[i])) > 0));
        }

        VERIFY(((scanf("%d", &temp)) == EOF));

        // Build the linked list
        struct Linked_List* head =  buildLinkedList(nodes, n, pos); 

        return head;
    } else {
        int n = atoi(argv[1]);
        int pos = atoi(argv[2]);
        int nodes[n];

        for (int i = 0; i < n; i++) {
            nodes[i] = atoi(argv[i+3]);
        }

        // Build the linked list
        struct Linked_List* head =  buildLinkedList(nodes, n, pos);

        return head;
    }
}