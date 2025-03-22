## Problem Description

Given the head of a singly linked list and two integers left and right, where 1 ≤ left ≤ right ≤ n (n is the number of nodes in the linked list), write a function to reverse the nodes of the list from position left to position right, and return the modified list.

## Input Format

The input consists of three lines:
1. The first line contains an integer n, the number of nodes in the linked list.
2. The second line contains n space-separated integers, representing the values of the nodes in the linked list.
3. The third line contains two space-separated integers, left and right, indicating the positions in the list to reverse between.

## Examples

### Example 1:

**Input:**
```
5
1 2 3 4 5
2 4
```

**Output:**
```
1 4 3 2 5
```

**Explanation:**
The original linked list is 1 → 2 → 3 → 4 → 5. After reversing from position 2 to 4, it becomes 1 → 4 → 3 → 2 → 5.

### Example 2:

**Input:**
```
3
10 20 30
1 2
```

**Output:**
```
20 10 30
```

**Explanation:**
The original linked list 10 → 20 → 30 is reversed from position 1 to 2, resulting in 20 → 10 → 30.

### Example 3:

**Input:**
```
1
42
1 1
```

**Output:**
```
42
```

**Explanation:**
A single-node linked list remains unchanged after reversal, even if left and right are both 1.

## Constraints:

1. The number of nodes in the list is in the range [1, 10⁴].
2. -10⁵ ≤ Node.val ≤ 10⁵.
3. 1 ≤ left ≤ right ≤ n.