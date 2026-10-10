# Variable Sized Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider an $n$-element array, $a$, where each index $i$ in the array contains a reference to an array of $k_i$ integers (where the value of $k_i$ varies from array to array). See the *Explanation* section below for a diagram.

Given $a$, you must answer $q$ queries. Each query is in the format `i j`, where $i$ denotes an index in array $a$ and $j$ denotes an index in the array located at $a[i]$. For each query, find and print the value of element $j$ in the array at location $a[i]$ on a new line.

Click [here](http://www.cplusplus.com/reference/vector/vector/) to know more about how to create variable sized arrays in C++.

**Input Format**

The first line contains two space-separated integers denoting the respective values of $n$ (the number of variable-length arrays) and $q$ (the number of queries).	
Each line $i$ of the $n$ subsequent lines contains a space-separated sequence in the format <code>k a[i]<sub>0</sub> a[i]<sub>1</sub> &hellip; a[i]<sub>k-1</sub></code> describing the $k$-element array located at $a[i]$.		
Each of the $q$ subsequent lines contains two space-separated integers describing the respective values of $i$ (an index in array $a$) and $j$ (an index in the array referenced by $a[i]$) for a query.

**Constraints**

- $1 \leq n \leq 10^5$
- $1 \leq q \leq 10^5$
- $1 \leq \ k \leq 3 \cdot 10^5$
- $n \leq \sum k \leq 3 \cdot 10^5$
- $0 \leq \ i < n$
- $0 \leq \ j < k$ 
- All indices in this challenge are zero-based.
- All the given numbers are non negative and are not greater than $10^6$

**Output Format**

For each pair of $i$ and $j$ values (i.e., for each query), print a single integer that denotes the element located at index $j$ of the array referenced by $a[i]$. There should be a total of $q$ lines of output.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T16:46:55.310Z  

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<vector<int>> a(n);
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        a[i].resize(k);
        for (int j = 0; j < k; j++) {
            cin >> a[i][j];
        }
    }

    while (q--) {
        int i, j;
        cin >> i >> j;
        cout << a[i][j] << "\n";
    }

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/variable-sized-arrays/problem)