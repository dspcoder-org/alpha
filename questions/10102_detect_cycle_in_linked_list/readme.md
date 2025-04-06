## Problem Description

Given the head of a singly linked list, write a function to detect if the linked list contains a cycle. If a cycle is present, return true; otherwise, return false.

## Examples

### Example 1:

**Input:**
```
4 1
1 2 3 4
```

**Output:**
```
true
```

**Explanation:**
The linked list has a cycle because the last node (4) points back to the node at index 1 (value 2).

### Example 2:

**Input:**
```
5 0
3 -3 4 0 2
```

**Output:**
```
true
```

**Explanation:**
The last node (value 2) links back to the head node, forming a cycle.

### Example 3:

**Input:**
```
3 -1
2 0 1
```

**Output:**
```
false
```

**Explanation:**
The linked list does not have a cycle, as there is no node linking back to a previous node.

## Constraints

1. The number of nodes in the list is in the range [0, 10⁴].
2. -10⁵ ≤ Node.val ≤ 10⁵