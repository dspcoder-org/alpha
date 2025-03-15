## Problem Description

Given the head of a singly linked list, your task is to reverse the list and return the reversed version.

## Examples

### Example 1:

**Input:**
```
5
1 2 3 4 5
```

**Output:**
```
5 4 3 2 1
```

**Explanation:**
The linked list `1 -> 2 -> 3 -> 4 -> 5` is reversed to `5 -> 4 -> 3 -> 2 -> 1`.



### Example 2:

**Input:**
```
1
1
```

**Output:**
```
1
```

**Explanation:**
The linked list `1 ` is reversed to `1` for single node.



### Example 3:

**Input:**
```
""
```

**Output:**
```
""
```

**Explanation:**
An empty linked list remains empty after reversal.



## Constraints:

1. The number of nodes in the list is in the range `[0, 10,000]`.
2. Each node's value satisfies `-10,000 ≤ Node.val ≤ 10,000`.