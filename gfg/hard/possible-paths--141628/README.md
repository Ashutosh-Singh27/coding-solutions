# Count Tree Paths With Limited Max Edge Weight

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a weighted tree with  **n**  nodes, numbered from 1 to n and n - 1 edges, where each edge is represented as [u, v, w] indicating an edge between nodes u and v with weight w.

You are also given an array  **queries[]**, where each queries[i] represents a maximum allowed edge weight.

For each query x, find the number of distinct paths in the tree such that the maximum edge weight along the path is less than or equal to x.

Return an array containing the number of valid paths for each query.

 **Note:** 

- A path from node u to node v and the path from node v to node u are considered the same path.
- A path must contain at least one edge. A path from a node to itself is not considered.

 **Examples:** 

```
Input: n = 3, edges[][] = [[1, 2, 1], [2, 3, 4]], queries[] = [3]
Output: [1]
Explanation:
For x = 3, only the edge [1, 2, 1] has weight less than or equal to 3.
Therefore, the only valid path is: 1 -> 2
The path 1 -> 3 contains an edge of weight 4, so it is not valid.
Hence, the answer is 1.
```

```
Input: n = 7, edges[][] = [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]], queries[] = [1, 3, 5]
Output: [1, 3, 4]
Explanation: For x = 1, only the edge [2, 3, 1] satisfies the condition. 
Therefore, the only valid path is 2 -> 3, giving an answer of 1.
For x = 3, the edges [2, 3, 1] and [1, 2, 3] can be used. 
They form three valid paths: 1 -> 2, 2 -> 3, and 1 -> 3. 
For x = 5, the edges with weights 1, 3, and 4 can be used. 
They form four valid paths: 1 -> 2, 2 -> 3, 1 -> 3, and 5 -> 7.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-03T14:44:17.646Z  

```py
class Solution:
    def maximumWeight(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges = sorted(edges, key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)

        j = 0
        pairs = 0
        for i in order:
            x = queries[i]
            while j < len(edges) and edges[j][2] <= x:
                u, v, _ = edges[j]
                ru, rv = find(u), find(v)
                if ru != rv:
                    pairs += size[ru] * size[rv]
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
                j += 1
            ans[i] = pairs
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/possible-paths--141628/1)