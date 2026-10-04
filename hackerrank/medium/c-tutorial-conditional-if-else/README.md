# Basic Data Types

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_if_ and _else_ are two of the most frequently used conditionals in C/C++, and they enable you to execute zero or one conditional statement among many such dependent conditional statements. We use them in the following ways:

1. *if:* This executes the body of bracketed code starting with $statement1$ if $condition$ evaluates to *true*.
	
    	if (condition) {
        	statement1;
            ...
        }

2. *if - else:* This executes the body of bracketed code starting with $statement1$ if $condition$ evaluates to *true*, or it executes the body of code starting with $statement2$ if $condition$ evaluates to *false*. Note that only *one* of the bracketed code sections will ever be executed.

		if (condition) {
        	statement1;
            ...
        }
        else {
            statement2;
        	...
        }

3. *if - else if - else:* In this structure, dependent statements are chained together and the $condition$ for each statement is only checked if all prior conditions in the chain evaluated to *false*. Once a $condition$ evaluates to *true*, the bracketed code associated with that statement is executed and the program then skips to the end of the chain of statements and continues executing. If each $condition$ in the chain evaluates to false, then the body of bracketed code in the *else* block at the end is executed.

		if(first condition) {
        	...
        }
        else if(second condition) {
        	...
        }
        .
        .
        .
        else if((n-1)'th condition) {
            ....
        }
        else {
        	...
        }
        
---

Given a positive integer $n$, do the following:

- If $1 \le n \le 9$, print the lowercase English word corresponding to the number (e.g., `one` for $1$, `two` for $2$, etc.).
- If $n \gt 9$, print `Greater than 9`.

**Input Format**

A single integer, $n$.

**Constraints**

- $1 \le n \le 10^9$

**Output Format**

If $1 \le n \le 9$, then print the lowercase English word corresponding to the number (e.g., `one` for $1$, `two` for $2$, etc.); otherwise, print `Greater than 9`.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T15:03:35.192Z  

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;

    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);

    printf("%d\n", a);
    printf("%ld\n", b);
    printf("%c\n", c);
    printf("%.3f\n", d);
    printf("%.9lf\n", e);
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem)