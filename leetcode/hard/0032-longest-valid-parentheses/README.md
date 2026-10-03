# Longest Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string containing just the characters `'('` and `')'`, return  *the length of the longest valid (well-formed) parentheses **substring*.

 

 **Example 1:** 

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

```

 **Example 2:** 

```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

```

 **Example 3:** 

```
Input: s = ""
Output: 0

```

 

 **Constraints:** 

- 0 <= s.length <= 3 * 104
- s[i] is '(', or ')'.

## Solution

**Language:** Java  
**Runtime:** 2 ms (beats 96.14%)  
**Memory:** 44.4 MB (beats 92.97%)  
**Submitted:** 2026-10-03T16:30:56.510Z  

```java
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0, max = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') left++;
            else right++;
            if (left == right) {
                max = Math.max(max, 2 * right);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }
        left = 0;
        right = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') left++;
            else right++;
            if (left == right) {
                max = Math.max(max, 2 * left);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }
        return max;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)