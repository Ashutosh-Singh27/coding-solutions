# Check if There Is a Valid Parentheses String Path

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

A parentheses string is a  **non-empty**  string consisting only of `'('` and `')'`. It is  **valid**  if  **any**  of the following conditions is  **true** :

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A  **valid parentheses string path**  in the grid is a path satisfying  **all**  of the following conditions:

- The path starts from the upper left cell (0, 0).
- The path ends at the bottom-right cell (m - 1, n - 1).
- The path only ever moves down or right.
- The resulting parentheses string formed by the path is valid.

Return `true`  *if there exists a  **valid parentheses string path**  in the grid.*  Otherwise, return `false`.

 

 **Example 1:** 

```
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

```

 **Example 2:** 

```
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either '(' or ')'.

## Solution

**Language:** Java  
**Runtime:** 4 ms (beats 97.14%)  
**Memory:** 48.8 MB (beats 88.57%)  
**Submitted:** 2026-09-29T08:13:33.490Z  

```java
class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        if ((m + n - 1) % 2 != 0) return false;
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;

        boolean[][][] visited = new boolean[m][n][m + n];
        return dfs(grid, 0, 0, 0, visited);
    }

    private boolean dfs(char[][] grid, int i, int j, int open, boolean[][][] visited) {
        int m = grid.length;
        int n = grid[0].length;

        if (i >= m || j >= n) return false;

        open += grid[i][j] == '(' ? 1 : -1;

        if (open < 0) return false;
        if (open > (m - i) + (n - j) - 2) return false;

        if (i == m - 1 && j == n - 1) return open == 0;

        if (visited[i][j][open]) return false;
        visited[i][j][open] = true;

        return dfs(grid, i + 1, j, open, visited) || dfs(grid, i, j + 1, open, visited);
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/)