# The If Statement

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number **n**, use the if statement to print " **Big** " (without quotes) if the given number is greater than 100. The statement " **Number** " (without quotes) will be printed regardless.

 **Note:** Follow Sample cases for the output format. After printing move the cursor to the next line.

 **Examples :** 

```
Input: n = 10
Output: 
Number
Explanation: 10 is less than 100, so we don't print Big and Number will be printed by default.

```

```
Input: n = 101
Output:
Big
Number
Explanation: 101 is greater than 100, so we print Big and Number will be printed by default in the next line.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T14:32:32.047Z  

```py
# code here
n=int(input())
if n<=100:
    print("Number")
else:
    print("Big\nNumber")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-if-statement--113256/1)