## Problem Description

Given the head of a singly linked list, write a function to find the middle element of the linked list.
If the list has an even number of nodes, return the second middle node.

## Examples

### Example 1:

**Input:**
```
5
1 2 3 4 5
```

**Output:**
```
3
```

**Explanation:**
The middle node in the odd-length list is the 3rd node.

### Example 2:

**Input:**
```
4
1 2 3 4
```

**Output:**
```
3
```

**Explanation:**
For an even-length list, return the second middle node (the 3rd node).

### Example 3:

**Input:**
```
1
42
```

**Output:**
```
42
```

**Explanation:**
For a single-node list, return that node.

## Constraints:

1. The number of nodes in the list is in the range `[1, 10,000]`.
2. Each node's value satisfies `-100,000 ≤ Node.val ≤ 100,000`.