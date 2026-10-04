# Learning to be Precise

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

There are times when your answer is a floating point that contains undesired amount of digits after decimal.

Here, we'll learn how to get a precise answer out of a floating number. You are given two floating numbers  **a**  and  **b**.

You need to print the value of  **a/b**  rounded to  **exactly 3**  decimal places.

- You may use library precision methods.
- You need to print the result (return type is void) without any spaces around it.

 **Example:** 

```
Input: a = 5.43, b = 2.653
Output: 2.047
Explanation: The exact result of a / b is approximately 2.04674. When rounded to 3 decimal places, it becomes 2.047.
```

```
Input: a = 10.0, b = 3.0
Output: 3.333
Explanation: 10 / 3 = 3.33333... → Rounded to 3 decimal places = 3.333
```

 **Constraints:** 
1 ≤ a, b ≤ 100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T14:57:47.846Z  

```py
class Solution:
    def precise(self, a, b):
        # code here
        print(f"{a/b:.3f}")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/learning-to-be-precise/1)