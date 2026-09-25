# Box Stacking

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given three arrays  **height[]**,  **width[]**, and  **length[]**  of size n, where height[i], width[i], and length[i] represent the dimensions of the ith box, find the maximum possible height of a stack formed using these boxes.

- A box can be rotated so that any of its dimensions becomes its height.
-  A box can be placed on top of another only if both dimensions of its base are strictly smaller than those of the box below. 
- Multiple instances of the same box can be used.

 **Examples:** 

```
Input: height[] = [4, 1, 4, 10], width[] = [6, 2, 5, 12], length[] = [7, 3, 6, 32]
Output: 60
Explanation: One possible arrangement of the boxes from bottom to top is shown below. Note that there can be multiple instances of a box type.
 
Hence, the total height of this stack is 10 + 32 + 4 + 4 + 6 + 1 + 3 = 60. No other combination of boxes produces a height greater than this.

```

```
Input: height[] = [1, 4, 3], width[] = [2, 5, 4], length[] = [3, 6, 1]
Output: 15
Explanation: One possible arrangement of the boxes from bottom to top is shown below: 

Hence, the total height of this stack is 4 + 6 + 1 + 1 + 3 = 15 No other combination of boxes produces a height greater than this.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T16:17:45.761Z  

```py
class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        n = len(height)
        boxes = []

        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            boxes.append((w, l, h))
            boxes.append((h, l, w))
            boxes.append((h, w, l))

        def normalize(box):
            w, l, h = box
            if w < l:
                w, l = l, w
            return (w, l, h)

        boxes = [normalize(b) for b in boxes]
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

        m = len(boxes)
        dp = [boxes[i][2] for i in range(m)]

        for i in range(1, m):
            for j in range(i):
                if boxes[j][0] > boxes[i][0] and boxes[j][1] > boxes[i][1]:
                    if dp[j] + boxes[i][2] > dp[i]:
                        dp[i] = dp[j] + boxes[i][2]

        return max(dp)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/box-stacking/1)