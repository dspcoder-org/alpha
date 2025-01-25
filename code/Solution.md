## How to Reverse a Linked List

Reversing a linked list involves changing the direction of the pointers in the list so that they point to the previous node instead of the next node. Here are the steps to reverse a linked list:

1. Initialize three pointers: `prev` as `NULL`, `current` as the head of the list, and `next` as `NULL`.
2. Iterate through the linked list. In each iteration:
   - Save the next node: `next = current->next`
   - Reverse the current node's pointer: `current->next = prev`
   - Move the pointers one position ahead: `prev = current` and `current = next`
3. After the loop, `prev` will be the new head of the reversed list.

#### Original Linked List
```
    head
  ____↓____         2                3                4                5
  ↓       ↓         ↑                ↑                ↑                ↑
[data | next]    [data | next] -> [data | next] -> [data | next] -> [data | next] 
  ↑      ↓_____________↑  ↓_____________↑  ↓_____________↑  ↓_____________↑   ↓
  1                                                                          NULL 
```

### Sample C Code

```c
void reverse_Linked_list(struct Linked_List** head) {
    // Write your code here
    struct Linked_List* prev = NULL;           // Previous node
    struct Linked_List* current = *head;       // Current node
    struct Linked_List* next = NULL;            // Next node

    while (current != NULL) {
        next = current->next;                   // Store the next node
        current->next = prev;                   // Reverse the current node's pointer
        prev = current;                         // Move prev and current one step forward
        current = next;
    }
    *head = prev; 
}
```