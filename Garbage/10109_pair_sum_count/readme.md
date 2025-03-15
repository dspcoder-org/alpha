## Problem Description

Given a list of integers and a target sum, your task is to determine the number of unique pairs of numbers in the list that add up to the given target sum. Each number in the list can be used at most once in a pair.

## Examples

### Example 1:

**Input:**
```
5
1 2 3 4 5
6
```

**Output:**
```
2
```

**Explanation:**
The pairs that sum to 6 are (1, 5) and (2, 4).

---

### Example 2:

**Input:**
```
4
3 3 3 3
6
```

**Output:**
```
2
```

**Explanation:**
The pairs that sum to 6 are (3, 3) and (3, 3), formed using different occurrences.

---

### Example 3:

**Input:**
```
5
0 -1 2 -3 1
-2
```

**Output:**
```
1
```

**Explanation:**
The valid pair that sums to -2 is (-3, 1).

---

## Constraints:

1. The number of integers in the array is in the range `[1, 100000]`.
2. Each element's value satisfies `-1000 ≤ Element value ≤ 1000`.
3. The target sum value satisfies `-10000 ≤ Target sum value ≤ 10000`.