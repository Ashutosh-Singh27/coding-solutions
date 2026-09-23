# The FizzBuzz Program

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n,**  print your answer according to the following conditions:

- If the number is divisible by 3, you print Fizz
- If the number is divisible by 5, you print Buzz
- If the number is divisible by both 3 and 5, you print FizzBuzz
- In any other case, you print the number itself

 **Examples:** 

```
Input: n = 3
Output: Fizz
Explanation: Here, the number is divisible by 3, so Fizz is printed.
```

```
Input: n = 5
Output: Buzz
Explanation: Here the number is divisible by 5, so Buzz is printed.
```

```
Input: number = 15
Output: FizzBuzz
Explanation: Here, the number 15 is divisible by both 3 and 5, so FizzBuzz is printed.

```

```
Input: number = 7
Output: 7
Explanation: 7 is not divisible by 3 or 5.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:53:56.537Z  

```py
n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-fizzbuzz-program/1)