#include <stdio.h>
#include <stdlib.h>

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


struct Linked_List* buildLinkedList(int arr[], int n){
    
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
    int n;
    
    // Input the number of elements
    scanf("%d", &n);

    // Create an array to store the node values
    int nodes[n];

    // Input the values into the array
    for (int i = 0; i < n; i++) {
        scanf("%d", &nodes[i]);
    }

    // Build the linked list
    struct Linked_List* head =  buildLinkedList(nodes, n); 

    return head;
}