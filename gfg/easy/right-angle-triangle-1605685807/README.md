# Solid Right Angle Triangle Pattern

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer **n**  **.** Write a program to print the Right angle triangle wall **.** The length of perpendicular and base is** s. 
Note: **Print exactly single " " after "** ***". Print a new line after printing the triangle.

 **Example:** 

```
Input: n = 4
Output:
* 
 **  
 **  * 
 **   **  
Explanation: Length of perpendicular and base of triangle is 4.
```

```
Input: n = 3
Output:
* 
 **  
 **  * 
Explanation: Length of perpendicular and base of triangle is 3.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T16:19:35.012Z  

```py
n = int(input())

# code here
for i in range(1, n+1):
    print("* "*i)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/right-angle-triangle-1605685807/1)