# Detect Loop in Linked List

## Problem Description
Given the head of a singly linked list, determine if the linked list has a cycle (loop) in it. A cycle exists if any node in the list can be reached again by continuously following the `next` pointer. Here instead of the `next` pointer of the last node (`tail`) pointing to `null`, it points to a node in the list.

## Examples

### Example 1:

```
    head
  ____↓____         2                0                4                
  ↓       ↓         ↑                ↑                ↑                
[data | next]    [data | next] -> [data | next] -> [data | next]  
  ↑      ↓_____________↑  ↓_____________↑  ↓_____________↑  |
  3                    ↑____________________________________|                
```

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2:
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3:
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

## Constraints:
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

## Notes:
- Do not modify the linked list.
- Your solution should use O(1) memory.
- The `pos` is used in the function signature to create the cycle for testing purposes. Your function should not use `pos`.

## Input Format
The input will be provided in the following format:
1. First line: An integer `n` representing the number of nodes in the linked list.
2. Second line: `n` space-separated integers representing the values of the nodes.
3. Third line: An integer `pos` representing the position of the node that the last node is connected to (-1 if there's no cycle).

## Output Format
Print "true" if there is a cycle in the linked list, "false" otherwise.

## Sample Input
```
4
3 2 0 -4
1
```

## Sample Output
```
true
```

## Explanation
The input creates a linked list: 3 -> 2 -> 0 -> -4
                                     ^         |
                                     |         |
                                     -----------
The last node (-4) is connected to the node at index 1 (2), forming a cycle.

Remember to handle edge cases properly, such as empty lists or lists with only one node.

Good luck!