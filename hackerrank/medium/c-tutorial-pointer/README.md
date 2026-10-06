# Pointer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A [pointer](http://en.wikipedia.org/wiki/Pointer_%28computer_programming%29) in C++ is used to share a memory address among different contexts (primarily functions). They are used whenever a function needs to modify the content of a variable, but it does not have ownership.  
<br>
In order to access the memory address of a variable, $val$, prepend it with $\&$ sign. For example, `&val` returns the memory address of $val$.  
<br>
This memory address is assigned to a pointer and can be shared among functions. For example, $int^* p = \&val$ assigns the memory address of $val$ to pointer $p$. To access the content of the memory pointed to, prepend the variable name with a `*`. For example, `*p` will return the value stored in $val$ and any modification to it will be performed on $val$.

	void increment(int *v) {
    	(*v)++;
    }
    
    int main() {
    	int a;
        scanf("%d", &a);
        increment(&a);
        printf("%d", a);
    	return 0;
    }  
    
**Function Description**  

Complete the *update* function in the editor below.  

*update* has the following parameters:  

- *int \*a:* an integer  
- *int \*b:* an integer  

**Returns**  

- The function is declared with a `void` return type, so there is no value to return. Modify the values in memory so that $a$ contains their sum and $b$ contains their absoluted difference.  

- $a' = a+b$
- $b' = |a-b|$

**Input Format**

Input will contain two integers, $a$ and $b$, separated by a newline.

**Constraints**

 

**Output Format**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T06:10:49.096Z  

```cpp
#include <stdio.h>
#include <stdlib.h>

void update(int *a, int *b) {
    int sum = *a + *b;
    int diff = abs(*a - *b);
    *a = sum;
    *b = diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/c-tutorial-pointer/problem)