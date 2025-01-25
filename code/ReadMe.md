## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1:

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

### Example 2:

```
Input: head = [1,2]
Output: [2,1]
```

### Example 3:

```
Input: head = []
Output: []
```

## Constraints:

- The number of nodes in the list is the range `[0, 10000]`.
- `-10000 <= Node.val <= 10000`

## Notes:

- The input is given as an array of integers which will be converted to a linked list internally.
- Your function should modify the original linked list structure.
- Do not return a new list; modify the original list in-place.
- After reversing, the `head` pointer should point to the new start of the list (previously the last element).

## Input Format

The input will be provided in the following format:
1. First line: An integer `n` representing the number of nodes in the linked list.
2. Second line: `n` space-separated integers representing the values of the nodes.

## Output Format

Print the values of the reversed linked list as space-separated integers on a single line.

## Sample Input

```
5
1 2 3 4 5
```

## Sample Output

```
5 4 3 2 1
```

## Explanation

The input creates a linked list: 1 -> 2 -> 3 -> 4 -> 5
After reversing, it becomes: 5 -> 4 -> 3 -> 2 -> 1

Remember to handle memory management properly to avoid memory leaks.

Good luck!
