# Range Vowel Count Queries

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string  **s**  and a 2D array  **queries[][]**, where each query consists of two integers  **l**  and  **r**, find the number of vowels in the substring  **s[l....r]**  for each query. The substring includes both indices l and r.

Return an array containing the answers to all queries in the order they are given.

 **Examples:** 

```
Input: s = "geeksforgeeks", queries[][] = [[1, 3], [2, 4], [1, 9]]
Output: [2, 1, 4]
Explanation:
Query 1: "eek" has 2 vowels (e, e).
Query 2: "eks" has 1 vowel (e).
Query 3: "eeksforge" has 4 vowels (e, e, o, e).
```

```
Input: s = "helloworld", queries[][] = [[0, 4], [5, 9], [0, 9]]
Output: [2, 1, 3]
Explanation:
Query 1: "hello" has 2 vowels (e, o).
Query 2: "world" has 1 vowel (o).
Query 3: "helloworld" has 3 vowels (e, o, o).
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-26T15:00:02.699Z  

```py
class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        n = len(s)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] + (ch in vowels)
        return [prefix[r + 1] - prefix[l] for l, r in queries]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/range-vowel-count-queries-static/1)