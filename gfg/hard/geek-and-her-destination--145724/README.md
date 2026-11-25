# Geek's Destination with Special Jump

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Geek starts at position  **0**  on the positive X-axis and needs to reach or pass position  **d**  on the positive X-axis.

Geek normally follows a repeating movement pattern:

- Move forward by a units, taking a seconds.
- Move backward by b units, taking b seconds.

Geek also has a special jump that moves him exactly  **j**  units forward in 1 second. He can use it at any time, even in the middle of a forward or backward movement, and the journey ends immediately after the jump.

Given five integers  **a**,  **b**,  **d**,  **l**, and  **r**. For every integer j in the range [l, r], find the minimum time required for Geek to reach or pass position d. He may either use the special jump or reach the destination using normal movement alone, whichever takes less time.

Return the sum of the minimum times for all jump lengths from l to r. Since, the answer can be large, return modulo 109 + 7. 

 **Note:** Each jump length is considered independently.

 **Examples:** 

```
Input: a = 2, b = 1, d = 5, l = 3, r = 4
Output: 5
Explanation: 
For j = 3, Geek moves 2 units forward, then takes a jump of 3 units to reach the destination. The minimum time required is 3 seconds.
For j = 4, Geek moves 1 unit forward, then takes a jump of 4 units to reach the destination. The minimum time required is 2 seconds.
Total sum for the range [l, r] = 3 + 2 = 5.
```

```
Input: a = 4, b = 2, d = 8, l = 2, r = 4
Output: 26
Explanation:
For j = 2, Geek moves 4 units forward, then 2 units backward. She then moves 4 units forward again and takes a jump of 2 units to reach the destination. The minimum time required is 11 seconds.
For j = 3, Geek moves 4 units forward, then 2 units backward. She then moves 3 units forward and takes a jump of 3 units to reach the destination. The minimum time required is 10 seconds.
For j = 4, Geek moves 4 units forward, then takes a jump of 4 units to reach the destination. The minimum time required is 5 seconds.
Total sum for the range [l, r] = 11 + 10 + 5 = 26.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T10:27:51.147Z  

```py
class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = max(a - b, 1)

        def F(u):
            if u <= 0:
                return 0
            q, rem = divmod(u, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        total = 0

        cnt_far = max(0, r - max(l, d) + 1)
        total += cnt_far

        if l < d:
            hi_j = min(r, d - 1)
            t_lo = d - hi_j
            t_hi = d - l
            cnt = t_hi - t_lo + 1
            sum_t = (t_lo + t_hi) * cnt // 2
            sum_k = F(t_hi - a) - F(t_lo - 1 - a)
            total += cnt + sum_t + 2 * b * sum_k

        return total % MOD
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/geek-and-her-destination--145724/1)