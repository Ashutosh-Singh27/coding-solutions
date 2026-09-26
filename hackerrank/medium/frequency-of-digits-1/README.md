# Digit Frequency

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string, $s$, consisting of alphabets and digits, find the frequency of each digit in the given string.

**Input Format**

The first line contains a string, $num$ which is the given number.

**Constraints**

$ 1 \le len(num) \le 1000$  
All the elements of num are made of english alphabets and digits.


**Output Format**

Print ten space-separated integers in a single line denoting the frequency of each digit from $0$ to $9$.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T07:55:14.233Z  

```c
#include <stdio.h>
#include <string.h>

int main() {
    char num[1001];
    scanf("%s", num);

    int freq[10] = {0};
    int len = strlen(num);

    for (int i = 0; i < len; i++) {
        if (num[i] >= '0' && num[i] <= '9') {
            freq[num[i] - '0']++;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", freq[i]);
    }
    printf("\n");

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/frequency-of-digits-1/problem)