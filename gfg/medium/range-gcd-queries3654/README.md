# Range GCD Queries

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]** and a 2D array **queries[][]**  containing  **q** queries, where each query is one of the following two types:

- Type 1: [0, l, r] -> Return the GCD of all elements in the range [l, r] (both inclusive).
- Type 2: [1, index, value] -> Update arr[index] to value.

Return an array containing the answers to all Type 1 queries in the order they appear in queries[][].

 **Note:** Use 0-based indexing.

 **Examples:** 

```
Input: arr[] = [2, 3, 4, 6, 8, 16], q = 3, queries[][] = [[0, 0, 2], [1, 3, 8], [0, 2, 5]]
Output: [1, 4]
Explanation: Initially, arr[] = [2, 3, 4, 6, 8, 16].
Query [0, 0, 2]: Find the GCD of the subarray arr[0...2] = [2, 3, 4]. The GCD is 1.
Query [1, 3, 8]: Update arr[3] from 6 to 8. The array becomes [2, 3, 4, 8, 8, 16].
Query [0, 2, 5]: Find the GCD of the subarray arr[2...5] = [4, 8, 8, 16]. The GCD is 4.
Therefore, the answers to all Type 0 queries are [1, 4].

```

```
Input: arr[] = [12, 18, 24, 30, 36], q = 4, queries[][] = [[0, 1, 3], [1, 2, 15], [0, 0, 2], [0, 2, 4]]
Output: [6, 3, 3]
Explanation: Initially, arr[] = [12, 18, 24, 30, 36].
Query [0, 1, 3]: Find the GCD of the subarray arr[1...3] = [18, 24, 30]. The GCD is 6.
Query [1, 2, 15]: Update arr[2] from 24 to 15. The array becomes [12, 18, 15, 30, 36].
Query [0, 0, 2]: Find the GCD of the subarray arr[0...2] = [12, 18, 15]. The GCD is 3.
Query [0, 2, 4]: Find the GCD of the subarray arr[2...4] = [15, 30, 36]. The GCD is 3.
Therefore, the answers to all Type 0 queries are [6, 3, 3].
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ q ≤ 105
0 ≤ l, r, index ≤ arr.size()-1
1 ≤ arr[i], value ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T11:51:29.897Z  

```py
from math import gcd

class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        tree = [0] * (2 * n)
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        result = []
        for t, a, b in queries:
            if t == 0:
                l = a + n
                r = b + n + 1
                g = 0
                while l < r:
                    if l & 1:
                        g = gcd(g, tree[l])
                        l += 1
                    if r & 1:
                        r -= 1
                        g = gcd(g, tree[r])
                    l >>= 1
                    r >>= 1
                result.append(g)
            else:
                i = a + n
                tree[i] = b
                i >>= 1
                while i >= 1:
                    tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
                    i >>= 1
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/range-gcd-queries3654/1)