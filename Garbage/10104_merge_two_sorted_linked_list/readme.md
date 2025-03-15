## Problem Description

Given the heads of two sorted singly linked lists, your task is to merge the two lists into a single sorted linked list.

## Examples

### Example 1:

**Input:**
```
3
1 2 4
3
1 3 4
```

**Output:**
```
1 1 2 3 4 4
```

**Explanation:**
The linked lists `1 -> 2 -> 4` and `1 -> 3 -> 4` are merged to `1 -> 1 -> 2 -> 3 -> 4 -> 4`.



### Example 2:

**Input:**
```
2
1 3
3
2 4 5
```

**Output:**
```
1 2 3 4 5
```

**Explanation:**
The linked lists `1 -> 3` and `2 -> 4 -> 5` are merged to `1 -> 2 -> 3 -> 4 -> 5`.



### Example 3:

**Input:**
```
0

0
```

**Output:**
```
""
```

**Explanation:**
Two empty linked lists remain empty after merging.



## Constraints:

1. The number of nodes in each list is in the range `[0, 10,000]`.
2. Each node's value satisfies `-10,000 ≤ Node.val ≤ 10,000`.