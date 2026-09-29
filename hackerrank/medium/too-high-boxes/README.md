# Boxes through a Tunnel

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are transporting some boxes through a tunnel, where each box is a  [parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped), and is characterized by its length, width and height.

The height of the tunnel $41$ feet and the width can be assumed to be infinite. A box can be carried through the tunnel only if its height is strictly less than the tunnel's height. Find the volume of each box that can be successfully transported to the other end of the tunnel. 
Note: Boxes cannot be rotated. 

**Input Format**

The first line contains a single integer $n$, denoting the number of boxes.  
$n$ lines follow with three integers on each separated by single spaces $-$ $length_i$, $width_i$ and $height_i$ which are length, width and height in feet of the $i$-th box.

**Constraints**

+ $1 \leq n \leq 100$
+ $1 \leq length_i,width_i,height_i \leq 100$

**Output Format**

For every box from the input which has a height lesser than $41$ feet, print its volume in a separate line.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T08:17:44.170Z  

```c

struct box
{
    int length;
    int width;
    int height;
};
typedef struct box box;

int get_volume(box b) {
    return b.length * b.width * b.height;
}

int is_lower_than_max_height(box b) {
    return b.height < MAX_HEIGHT;
}


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/too-high-boxes/problem)