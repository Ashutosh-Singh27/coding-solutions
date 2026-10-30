# Tuples

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Task** 
Given an integer,, and space-separated integers as input, create a tuple,, of those integers. Then compute and print the result of.

 **Note:**  hash() is one of the functions in the `__builtins__` module, so it need not be imported.

 **Input Format** 

The first line contains an integer,, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple.

 **Output Format** 

Print the result of.

 **Sample Input 0** 

```
2
1 2

```

 **Sample Output 0** 

```
3713081631934410656

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T08:13:10.117Z  

```py
def old_tuple_hash(t):
    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    length = len(t)
    for item in t:
        length -= 1
        x = ((x ^ hash(item)) * mult) & mask
        mult = (mult + 82520 + length + length) & mask
    x = (x + 97531) & mask
    if x >= 1 << 63:
        x -= 1 << 64
    if x == -1:
        x = -2
    return x

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(old_tuple_hash(t))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-tuples/problem)