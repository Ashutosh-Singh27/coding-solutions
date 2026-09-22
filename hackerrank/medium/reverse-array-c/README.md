# 1D Arrays in C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array, of size $n$, reverse it.

Example: If array, $arr = [1, 2, 3, 4, 5]$, after reversing it, the array should be, $arr = [5, 4, 3, 2, 1]$.

**Input Format**

The first line contains an integer, $n$, denoting the size of the array.
The next line contains $n$ space-separated integers denoting the elements of the array.

**Constraints**

$ 1 \le n \le 1000$  
$ 1 \le arr_i \le 1000$, where $arr_i$ is the $i^{th}$ element of the array.

**Output Format**

The output is handled by the code given in the editor, which would print the array.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T11:22:26.837Z  

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    printf("%d\n", sum);

    free(arr);

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/reverse-array-c/problem)