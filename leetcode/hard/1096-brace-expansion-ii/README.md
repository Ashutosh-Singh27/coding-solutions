# Brace Expansion II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The grammar can best be understood through simple examples:

- Single letters represent a singleton set containing that word. R("a") = {"a"} R("w") = {"w"}
- When we take a comma-delimited list of two or more expressions, we take the union of possibilities. R("{a,b,c}") = {"a","b","c"} R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
- When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression. R("{a,b}{c,d}") = {"ac","ad","bc","bd"} R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the three rules for our grammar:

- For every lowercase letter x, we have R(x) = {x}.
- For expressions e1, e2,..., ek with k >= 2, we have R({e1, e2,...}) = R(e1) ∪ R(e2) ∪...
- For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return  *the sorted list of words that the expression represents*.

 

 **Example 1:** 

```
Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

```

 **Example 2:** 

```
Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

```

 

 **Constraints:** 

- 1 <= expression.length <= 60
- expression[i] consists of '{', '}', ','or lowercase English letters.
- The given expression represents a set of words based on the grammar given in the description.

## Solution

**Language:** Java  
**Runtime:** 10 ms (beats 68.80%)  
**Memory:** 47.1 MB (beats 72.00%)  
**Submitted:** 2026-09-25T15:55:00.494Z  

```java
class Solution {
    private String expr;
    private int pos;

    public List<String> braceExpansionII(String expression) {
        this.expr = expression;
        this.pos = 0;
        Set<String> result = parseExpr();
        List<String> answer = new ArrayList<>(result);
        Collections.sort(answer);
        return answer;
    }

    private Set<String> parseExpr() {
        Set<String> result = new HashSet<>();
        result.addAll(parseTerm());
        while (pos < expr.length() && expr.charAt(pos) == ',') {
            pos++;
            result.addAll(parseTerm());
        }
        return result;
    }

    private Set<String> parseTerm() {
        List<Set<String>> factors = new ArrayList<>();
        while (pos < expr.length() && expr.charAt(pos) != ',' && expr.charAt(pos) != '}') {
            factors.add(parseFactor());
        }
        return concatFactors(factors);
    }

    private Set<String> parseFactor() {
        if (expr.charAt(pos) == '{') {
            pos++;
            Set<String> result = parseExpr();
            pos++;
            return result;
        } else {
            int start = pos;
            while (pos < expr.length() && Character.isLowerCase(expr.charAt(pos))) {
                pos++;
            }
            Set<String> result = new HashSet<>();
            result.add(expr.substring(start, pos));
            return result;
        }
    }

    private Set<String> concatFactors(List<Set<String>> factors) {
        Set<String> result = new HashSet<>();
        result.add("");
        for (Set<String> factor : factors) {
            Set<String> temp = new HashSet<>();
            for (String prefix : result) {
                for (String word : factor) {
                    temp.add(prefix + word);
                }
            }
            result = temp;
        }
        return result;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/brace-expansion-ii/)