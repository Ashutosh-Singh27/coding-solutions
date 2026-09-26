# Inverted Right Angle Triangle Pattern

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer **n**  **.** Write a program to print the inverted "Right angle triangle" wall **.** The length of the perpendicular and base is **n.** 

 **Examples:** 

```
Input: n = 5
Output:
  *
  
*** 
**
*
Explanation: Length of perpendicular and base of triangle is 5.
```

```
Input: n = 3
Output:
*** 
** 
*
Explanation: Length of perpendicular and base of triangle is 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T08:01:45.569Z  

```py
n = int(input())

# code here
for i in range(n, 0, -1):
    print('*'*i)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/inverted-right-angletriangle-1605691171--104349/1)