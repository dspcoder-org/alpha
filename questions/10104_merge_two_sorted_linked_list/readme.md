## Problem Description

Given two sorted linked lists, write a function to merge them into a single sorted linked list. The new list should be made by splicing together the nodes of the first two lists.

## Examples

### Example 1:

**Input:**
```
1 2 4
1 3 4
```

**Output:**
```
1 1 2 3 4 4
```

**Explanation:**
Merge the two sorted lists by comparing and ordering the nodes.

### Example 2:

**Input:**
```
0 3 6
1 2 5
```

**Output:**
```
0 1 2 3 5 6
```

**Explanation:**
Merge the two sorted lists maintaining the sorted order.

### Example 3:

**Input:**
```
[]
0 1 2
```

**Output:**
```
0 1 2
```

**Explanation:**
If one list is empty, return the other list.

## Constraints:

1. The number of nodes in each list is in the range `[0, 50]`.
2. Each node's value satisfies `-10⁵ ≤ Node.val ≤ 10⁵`.
3. Both input lists are sorted in non-decreasing order.