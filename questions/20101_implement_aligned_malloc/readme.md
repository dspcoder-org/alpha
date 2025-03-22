## Problem Description

Given a required alignment and size, write a function to allocate memory with a specific alignment constraint. The function should return a pointer to the aligned memory block, which can be freed later.

## Examples

### Example 1:

**Input:**
```
16 8
```

**Output:**
```
<pointer to 8-byte aligned memory block of 16 bytes>
```

**Explanation:**
Allocated 16 bytes of memory with 8-byte alignment.

### Example 2:

**Input:**
```
100 64
```

**Output:**
```
<pointer to 64-byte aligned memory block of 100 bytes>
```

**Explanation:**
Allocated 100 bytes of memory with 64-byte alignment.

### Example 3:

**Input:**
```
10 4
```

**Output:**
```
<pointer to 4-byte aligned memory block of 10 bytes>
```

**Explanation:**
Allocated 10 bytes of memory with 4-byte alignment.

## Constraints:

1. The size is in the range `[1, 10^8]`.
2. The alignment is a power of 2 (e.g., 2, 4, 8, 16, 32, 64, 128, etc.).
3. You can use standard malloc and other standard C library functions.