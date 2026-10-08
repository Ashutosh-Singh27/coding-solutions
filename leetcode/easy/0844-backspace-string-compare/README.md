# Backspace String Compare

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true`  *if they are equal when both are typed into empty text editors*. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

 **Example 1:** 

```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

```

 **Example 2:** 

```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

```

 **Example 3:** 

```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

```

 

 **Constraints:** 

- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

 

 **Follow up:**  Can you solve it in `O(n)` time and `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 25.87%)  
**Submitted:** 2026-10-08T06:24:02.708Z  

```py
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(x):
            stack = []
            for ch in x:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return stack
        return build(s) == build(t)
```

---

[View on LeetCode](https://leetcode.com/problems/backspace-string-compare/)