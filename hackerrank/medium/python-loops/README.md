# Loops

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Check Tutorial tab to know how to to solve.

 **Task** 
The provided code stub reads an integer,, from STDIN. For all non-negative integers, print.

 **Example** 

The list of non-negative integers that are less than is. Print the square of each number on a separate line.

```
0
1
4

```

 **Input Format** 

The first and only line contains the integer,.

 **Constraints** 

 **Output Format** 

Print lines, one corresponding to each.

 **Sample Input 0** 

```
5

```

 **Sample Output 0** 

```
0
1
4
9
16

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T10:52:56.981Z  

```py
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-loops/problem)