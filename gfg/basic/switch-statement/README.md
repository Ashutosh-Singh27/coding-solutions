# Switch Statement

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**, use a switch statement to return "One" if the given number is equal to 1, "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

 **Examples:** 

```
Input: n = 10
Output: Unknown
```

```
Input: n = 1
Output: One
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T17:26:52.986Z  

```py
n = int(input())

names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
         6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
print(names.get(n, "Unknown"))
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/switch-statement/1)