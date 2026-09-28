# Jumping through While - Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive integer  **x**, the task is to print the numbers from  **1 to x**  in the order as  **12, 22, 32, 42, 52,...**  (in increasing order).

 **Example:** 

```
Input: x = 10
Output: 1 4 9
Explanation:From 1 to 10, numbers in powers of 2 are, 12, 22, 32 as 1, 4 and 9.
```

 **Constraints** :
2 <= x <= 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T11:57:56.387Z  

```py
def printIncreasingPower(x):
    i = 1
    while i * i <= x:
        print(i * i, end=" ")
        i += 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/jumping-through-while-python/1)