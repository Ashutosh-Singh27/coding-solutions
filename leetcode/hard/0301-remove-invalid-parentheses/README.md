# Remove Invalid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return  *a list of  **unique strings**  that are valid with the minimum number of removals*. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "()())()"
Output: ["(())()","()()()"]

```

 **Example 2:** 

```
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

```

 **Example 3:** 

```
Input: s = ")("
Output: [""]

```

 

 **Constraints:** 

- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'.
- There will be at most 20 parentheses in s.

## Solution

**Language:** Python  
**Runtime:** 1196 ms (beats 23.18%)  
**Memory:** 19.5 MB (beats 62.94%)  
**Submitted:** 2026-10-07T05:53:47.012Z  

```py
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = set()

        def dfs(i, l, r, open_count, path):
            if i == len(s):
                if l == 0 and r == 0 and open_count == 0:
                    res.add("".join(path))
                return
            c = s[i]
            if c == '(' and l > 0:
                dfs(i + 1, l - 1, r, open_count, path)
            elif c == ')' and r > 0:
                dfs(i + 1, l, r - 1, open_count, path)
            path.append(c)
            if c == '(':
                dfs(i + 1, l, r, open_count + 1, path)
            elif c == ')':
                if open_count > 0:
                    dfs(i + 1, l, r, open_count - 1, path)
            else:
                dfs(i + 1, l, r, open_count, path)
            path.pop()

        dfs(0, left, right, 0, [])
        return list(res)
```

---

[View on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)