# Arithmetic Operators

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two integer variables x and y, perform the following operations:

- p: Addition of x and y
- q: Subtraction of y from x
- r: Multiplication of x and y
- s: Floating-point division of x by y
- t: Integer division of x by y
- u: Modulo (remainder when x is divided by y)

 **Examples:** 

```
Input: x = 1, y = 2
Output: 3 -1 2 0.500 0 1
Explanation: The given operations are performed:
Addition of x and y = 3
Subtraction of y from x = -1
Multiplication of x and y = 2
Floating-point division of x by y = 0.500
Integer division of x by y = 0
Modulo of x and y = 1
Hence, the output is 3 -1 2 0.500 0 1.

```

```
Input: x = 3, y = 4 
Output: 7 -1 12 0.750 0 3
Explanation: The given operations are performed.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:30:43.357Z  

```py
x = int(input())
y = int(input())

# code here
p = x + y
q = x - y
r = x * y
s = x / y
t = x // y
u = x % y
print(p, q, r, f"{s:.3f}", t, u)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/arithmetic-operators/1)