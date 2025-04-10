## Problem Description

Given the head of a sorted singly linked list, write a function to remove all duplicates such that each element appears only once. The function should return the head of the updated linked list with all duplicates removed.

## Input Format

The input consists of two lines:
1. The first line contains an integer n, the number of nodes in the linked list.
2. The second line contains n space-separated integers, representing the values of the nodes in the linked list. The list is sorted in non-decreasing order.

## Examples

### Example 1:

**Input:**
```
5
1 1 2 3 3
```

**Output:**
```
1 2 3
```

**Explanation:**
The original linked list is 1 → 1 → 2 → 3 → 3. After removing duplicates, it becomes 1 → 2 → 3.

### Example 2:

**Input:**
```
4
10 10 20 30
```

**Output:**
```
10 20 30
```

**Explanation:**
The original linked list 10 → 10 → 20 → 30 is updated to 10 → 20 → 30 after removing duplicates.

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
A single-node linked list remains unchanged as there are no duplicates to remove.

## Constraints:

1. The number of nodes in the list is in the range `[0, 10⁴]`.
2. Each node's value satisfies `-10⁵ ≤ Node.val ≤ 10⁵`.
3. The linked list is sorted in non-decreasing order.