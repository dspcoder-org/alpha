#include <stdio.h>
#include <stdlib.h>

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
extern struct Linked_List* setup_question(int argc, char* argv[], struct Linked_List** headB);
extern void print_Intersection(struct Linked_List* intersection);

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

void print_Intersection(struct Linked_List* intersection){
    if(intersection == NULL){
        printf("null\n");
    } else {
        printf("%d\n", intersection->data);
    }
}

struct Linked_List* setup_question(int argc, char* argv[], struct Linked_List** headB) {

    if (argc == 1) {
        int n, m, temp;
        
        // Input the number of elements for the first list
        VERIFY(((scanf("%d", &n)) > 0));

        // Create an array to store the node values for the first list
        int nodesA[n];

        // Input the values into the array for the first list
        for (int i = 0; i < n; i++) {
            VERIFY(((scanf("%d", &nodesA[i])) > 0));
        }

        // Input the number of elements for the second list
        VERIFY(((scanf("%d", &m)) > 0));

        // Create an array to store the node values for the second list
        int nodesB[m];

        // Input the values into the array for the second list
        for (int i = 0; i < m; i++) {
            VERIFY(((scanf("%d", &nodesB[i])) > 0));
        }

        VERIFY(((scanf("%d", &temp)) == EOF));

        // Build the linked lists
        struct Linked_List* headA = buildLinkedList(nodesA, n);
        *headB = buildLinkedList(nodesB, m);

        return headA;
    } else {
        int n = atoi(argv[1]);
        int nodesA[n];

        for (int i = 0; i < n; i++) {
            nodesA[i] = atoi(argv[i+2]);
        }

        int m = atoi(argv[n+2]);
        int nodesB[m];

        for (int i = 0; i < m; i++) {
            nodesB[i] = atoi(argv[n+3+i]);
        }

        // Build the linked lists
        struct Linked_List* headA = buildLinkedList(nodesA, n);
        *headB = buildLinkedList(nodesB, m);

        return headA;
    }
}