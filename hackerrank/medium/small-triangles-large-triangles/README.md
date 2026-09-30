# Small Triangles, Large Triangles

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given $n$ triangles, specifically, their sides $a_i$, $b_i$ and $c_i$. Print them in the same style but sorted by their areas from the smallest one to the largest one. It is guaranteed that all the areas are different.

The best way to calculate a area of a triangle with sides $a$, $b$ and $c$ is Heron's formula:

$S = \sqrt{p \times (p-a) \times (p-b) \times (p-c)}$ where $p={\frac {a+b+c} 2}$.


**Input Format**

The first line of each test file contains a single integer $n$. $n$ lines follow with three space-separated integers, $a_i$, $b_i$ and $c_i$.

**Constraints**

+ $1 \leq n \leq 100$
+ $1 \leq a_i,b_i,c_i \leq 70$
+ $a_i+b_i>c_i$,$a_i+c_i>b_i$ and $b_i+c_i>a_i$

**Output Format**

Print exactly $n$ lines. On each line print $3$ space-separated integers, the $a_i$, $b_i$ and $c_i$ of the corresponding triangle.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T13:49:41.399Z  

```c

double area(triangle t) {
    double p = (t.a + t.b + t.c) / 2.0;
    return sqrt(p * (p - t.a) * (p - t.b) * (p - t.c));
}

void sort_by_area(triangle* tr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (area(tr[j]) > area(tr[j + 1])) {
                triangle temp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp;
            }
        }
    }
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem)