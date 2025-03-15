## Problem Description

Given the head of a singly linked list, your task is to check if the list represents a palindrome. A linked list is a palindrome if the sequence of values reads the same forward and backward.

## Examples

### Example 1:

**Input:**
```
5
1 2 3 2 1
```

**Output:**
```
true
```

**Explanation:**
The linked list `1 -> 2 -> 3 -> 2 -> 1` reads the same forward and backward, making it a palindrome.



### Example 2:

**Input:**
```
4
1 2 2 1
```

**Output:**
```
true
```

**Explanation:**
The linked list `1 -> 2 -> 2 -> 1` is a palindrome as it is symmetric.



### Example 3:

**Input:**
```
3
1 2 3
```

**Output:**
```
false
```

**Explanation:**
The linked list `1 -> 2 -> 3` is not a palindrome because 1 ≠ 3.



## Constraints:

1. The number of nodes in the list is in the range `[0, 10,000]`.
2. Each node's value satisfies `-100,000 ≤ Node.val ≤ 100,000`.