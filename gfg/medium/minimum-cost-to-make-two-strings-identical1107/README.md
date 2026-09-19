# Min Cost To Make Two Strings Identical

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings  **s1**  and  **s2**, and two integers  **costS1**  and  **costS2**, where costS1 is the cost of deleting one character from s1 and costS2 is the cost of deleting one character from s2, find the minimum cost required to make the two strings identical.

You can delete any number of characters from either string, but the order of the remaining characters must be preserved.

 **Examples:** 

```
Input: s1 = "abcd", s2 = "acdb", costS1 = 10, costS2 = 20
Output: 30
Explanation: Delete 'b' from both strings to obtain "acd". The total cost is 10 + 20 = 30.
```

```
Input: s1 = "ef", s2 = "gh", costS1 = 10, costS2 = 20
Output: 60
Explanation: The two strings have no common characters, so delete all characters from both strings. The total cost is (2 × 10) + (2 × 20) = 60.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T15:29:19.281Z  

```py
class Solution:
    def findMinCost(self, s1, s2, costS1, costS2):
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[n][m]
        return (n - lcs) * costS1 + (m - lcs) * costS2
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1)