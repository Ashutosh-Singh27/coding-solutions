# Longest Matching in Dictionary with Removals

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a lowercase string  **s**  and a dictionary  **d[]**  containing lowercase words, find the longest word in the dictionary that can be obtained by deleting some characters from s without changing the order of the remaining characters.

 **Note** : If multiple words have the same maximum length, return the lexicographically smallest one. If no valid word exists, return an empty string.

 **Examples :** 

```
Input: d = ["ale", "apple", "monkey", "plea"], s = "abpcplea"
Output: "apple" 
Explanation: After deleting "b", "c", "a" s became "apple" which is present in d.

```

```
Input: d = ["a", "b", "c"], s = "abpcplea"
Output: "a"
Explanation: After deleting "b", "p", "c", "p", "l", "e", "a" s became "a" which is present in d.
```

 **Constraints:** 
1 ≤ |s| ≤ 5 * 105
1 ≤ n ≤ 104, where n is the number of words in dictionary
1 ≤ m ≤ 100, where m is the length of word in dictionary
s and all words in dictionary consist only of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T12:51:39.507Z  

```py
from bisect import bisect_left

class Solution:
    def findLongestWord(self, s, d):
        positions = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            positions[ord(ch) - 97].append(i)

        def isSubsequence(word):
            pos = -1
            for ch in word:
                lst = positions[ord(ch) - 97]
                idx = bisect_left(lst, pos + 1)
                if idx == len(lst):
                    return False
                pos = lst[idx]
            return True

        result = ""
        for word in d:
            if isSubsequence(word):
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1)