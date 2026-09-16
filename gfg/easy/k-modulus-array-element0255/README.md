# Values with Equal Array Remainders

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array  **arr[]**, count the number of positive integers  **k**  such that all elements of the array leave the same remainder when divided by k.

If there are infinitely many such values of k, return  **-1**.

 **Examples:** 

```
Input: arr[] = [38, 6, 34]
Output: 3
Explanation: 
The values of k for which all elements leave the same remainder when divided by k are 1, 2, and 4.
For k = 1, all elements leave remainder 0.
For k = 2, all elements leave remainder 0.
For k = 4, all elements leave remainder 2.
No other positive integer satisfies the required condition. Hence, the answer is 3.
```

```
Input: arr[] = [3, 2]
Output: 1
Explanation: 
The only positive integer for which both elements leave the same remainder is 1, 
since both numbers leave remainder 0 when divided by 1.
```

```
Input: arr[] = [5, 5, 5]
Output: -1
Explanation: 
All elements in the array are equal. Therefore, for every positive integer k, 
all elements leave the same remainder when divided by k.
Since there are infinitely many such values of k, the answer is -1.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T17:32:53.510Z  

```py
import math

class Solution:
    def sameMod(self, arr):
        if all(x == arr[0] for x in arr):
            return -1

        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

        # count divisors of g
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1

        return count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/k-modulus-array-element0255/1)