# Printing Tokens

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a sentence, $s$, print each word of the sentence in a new line.

**Input Format**

The first and only line contains a sentence, $s$.

**Constraints**

$ 1 \le len(s) \le 1000$  

**Output Format**

Print each word of the sentence in a new line.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:56:02.419Z  

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[1001];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';
    char *token = strtok(s, " ");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, " ");
    }
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/printing-tokens-/problem)