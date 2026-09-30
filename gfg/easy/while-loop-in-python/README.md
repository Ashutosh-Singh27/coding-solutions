# While loop in Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

**Congratulations!**  You are one more step close to Python Programming World. You are now familiar with  **if-elif-else**  in Python, and  **for**  loop in Python.

While loop in Python is same as like in CPP and Java, but, here you have to use ' **:** ' to end while statement (used to end any statement). While loop is used to iterate same as for loop, except that in while loop you can customize jump of steps in coupling with variable used to loop, after every iteration, unlike in for loop (you cannot customize jump according to the variable you are using to loop through).

Let's get it more clearly through this question. Given a number  **x**, the task is to print the numbers from x to 0 in  **decreasing order**  in a single line.

 **Example:** 

```
Input: x = 3
Output: 3 2 1 0
Explanation:
Numbers in decreasing order from 3
are 3, 2, 1, 0.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T13:29:24.810Z  

```py
def printInDecreasing(x):
    # code here
    while (x >= 0):
        print(x, end=" ")

        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code

        x -= 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/while-loop-in-python/1)