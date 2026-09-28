# Variadic functions in C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Variadic functions are functions which take a variable number of arguments.  In C programming, a variadic function will contribute to the flexibility of the program that you are developing.

The declaration of a variadic function starts with the declaration of at least one named variable, and uses an ellipsis as the last parameter, 
e.g. 

```
int printf(const char* format, ...);
```
In this problem, you will implement three variadic functions named $sum()$, $min()$ and  $max()$ to calculate sums, minima, maxima of a variable number of arguments.  The first argument passed to the variadic function is the count of the number of arguments, which is followed by the arguments themselves.  
  


**Input Format**

- The first line of the input consists of an integer $number\_of\_test\_cases$.  
- Each test case tests the logic of your code by sending a test implementation of 3, 5 and 10 elements respectively.  
- You can test your code against sample/custom input.  
- The error log prints the parameters which are passed to the test implementation.  It also prints the sum, minimum element and maximum element corresponding to your code.   

**Constraints**

$1 \enspace \le \enspace number\_of\_test\_cases \enspace \le 50 $  
$1 \le element \le 1000000$ . 

**Output Format**

"Correct Answer" is printed corresponding to each correct execution of a test implementation."Wrong Answer" is printed otherwise.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T12:23:07.104Z  

```c

int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    va_end(args);
    return total;
}

int min(int count, ...) {
    va_list args;
    va_start(args, count);
    int result = va_arg(args, int);
    for (int i = 1; i < count; i++) {
        int value = va_arg(args, int);
        if (value < result) {
            result = value;
        }
    }
    va_end(args);
    return result;
}

int max(int count, ...) {
    va_list args;
    va_start(args, count);
    int result = va_arg(args, int);
    for (int i = 1; i < count; i++) {
        int value = va_arg(args, int);
        if (value > result) {
            result = value;
        }
    }
    va_end(args);
    return result;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/variadic-functions-in-c/problem)