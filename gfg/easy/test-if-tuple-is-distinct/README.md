# Test if tuple is distinct

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a tuple  **arr** , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

 **Examples:** 

```
Input: arr = (1, 2, 3, 4, 5, 4)
Output: False
```

```
Input: arr = (1, 2, 3, 4, 5)
Output: True
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T15:54:22.534Z  

```py
arr = tuple(map(int, input().split()))

# code here
if len(set(arr))==len(arr):
    print("True")
else:
    print("False")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/test-if-tuple-is-distinct/1)