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
extern void setup_question(struct Linked_List** list1, struct Linked_List** list2);
extern void print_LinkedList(struct Linked_List* head);

// end of util.h

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



void setup_question(struct Linked_List** list1, struct Linked_List** list2){
    int n1, n2, temp;
    
    // Input the number of elements for the first list
    VERIFY(((scanf("%d", &n1)) > 0));

    // Create an array to store the node values for the first list
    int nodes1[n1];

    // Input the values into the array for the first list
    for (int i = 0; i < n1; i++) {
        VERIFY(((scanf("%d", &nodes1[i])) > 0));
    }

    // Input the number of elements for the second list
    VERIFY(((scanf("%d", &n2)) > 0));

    // Create an array to store the node values for the second list
    int nodes2[n2];

    // Input the values into the array for the second list
    for (int i = 0; i < n2; i++) {
        VERIFY(((scanf("%d", &nodes2[i])) > 0));
    }

    VERIFY(((scanf("%d", &temp)) == EOF));

    // Build the linked lists
    *list1 = buildLinkedList(nodes1, n1);
    *list2 = buildLinkedList(nodes2, n2);


}