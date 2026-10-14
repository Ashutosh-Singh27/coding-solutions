# Vector-Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given $N$ integers.Sort the $N$ integers and print the sorted order.<br>
Store the $N$ integers in a vector.Vectors are sequence containers representing arrays that can change in size.

- *Declaration:*

		vector<int>v; (creates an empty vector of integers)
- *Size:*
		
        int size=v.size();
        
- *Pushing an integer into a vector:*

		v.push_back(x);(where x is an integer.The size increases by 1 after this.)
     
- *Popping the last element from the vector:*

		v.pop_back(); (After this the size decreases by 1)
        
- *Sorting a vector:*

		sort(v.begin(),v.end()); (Will sort all the elements in the vector)
        
To know more about vectors, [Click Here](http://www.cplusplus.com/reference/vector/vector/)


**Input Format**

The first line of the input contains $N$ where $N$ is the number of integers. The next line contains $N$ integers.<br>
**Constraints**<br>
$1<=N<=10^5$<br>
$1<=V_i<=10^9$, where $V_i$ is the $i^{th}$ integer in the vector.

**Output Format**

Print the integers in the sorted order one by one in a single line followed by a space.<br>

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T11:05:12.843Z  

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/vector-sort/problem)