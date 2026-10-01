# Minimum Time to Finish Project

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An IT company is working on a large project consisting of  **n**  modules.

- The given array time required (in months) to complete the ith module is stored in the array duration[].
- The array dependencies[][], where dependencies[i] = [u, v], indicates that module v can be started only after module u is completed. 

Multiple modules can be worked on simultaneously as long as all their dependencies have been completed.

Find the minimum time required to complete the entire project.

- If the project cannot be completed due to a cyclic dependency, return -1.
- A module is never dependent on itself.

 **Examples** 

```
Input: duration[] = [10, 20, 30, 10, 30, 20], dependencies[][] = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
Output: 80
Explanation: 

The Graph of dependency forms this and the project will be completed when Module 1 is completed. The minimum taken time is 80 months, the maximum taken time is through the path 5 -> 2 -> 3 -> 1 which takes 20 + 30 + 10 + 20
```

```
Input: duration[] = [5, 5, 5], dependencies[][] = [[0, 1], [1, 2], [2, 0]]
Output: -1
Explanation: There is a cycle in the dependency graph hence the project cannot be completed.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T15:51:59.980Z  

```py
from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1

        finish = [0] * n
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                finish[i] = duration[i]

        processed = 0
        while queue:
            u = queue.popleft()
            processed += 1
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + duration[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        if processed != n:
            return -1
        return max(finish)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/project-manager--141631/1)