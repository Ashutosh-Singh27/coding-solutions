# Maximum Number of Non-Overlapping Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` of lowercase letters, you need to find the maximum number of  **non-empty**  substrings of `s` that meet the following conditions:

- The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
- A substring that contains a certain character c must also contain all occurrences of c.

Find  *the maximum number of substrings that meet the above conditions*. If there are multiple solutions with the same number of substrings,  *return the one with minimum total length.* It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in  **any**  order.

 

 **Example 1:** 

```
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

```

 **Example 2:** 

```
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s contains only lowercase English letters.

## Solution

**Language:** Java  
**Runtime:** 8 ms (beats 96.16%)  
**Memory:** 47.9 MB (beats 88.24%)  
**Submitted:** 2026-09-18T13:13:50.376Z  

```java
class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        List<int[]> intervals = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) continue;
            int start = first[i];
            int end = last[i];
            boolean valid = true;
            int j = start;
            while (j <= end) {
                int c = s.charAt(j) - 'a';
                if (first[c] < start) {
                    valid = false;
                    break;
                }
                if (last[c] > end) end = last[c];
                j++;
            }
            if (valid) intervals.add(new int[]{start, end});
        }
        intervals.sort((a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);
        List<String> res = new ArrayList<>();
        int prevEnd = -1;
        for (int[] iv : intervals) {
            if (iv[0] > prevEnd) {
                res.add(s.substring(iv[0], iv[1] + 1));
                prevEnd = iv[1];
            }
        }
        return res;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)