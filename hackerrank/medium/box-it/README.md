# Box It!

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Design a class named *Box* whose dimensions are integers and private to the class. The dimensions are labelled: length $l$, breadth $b$, and height $h$. 

The default constructor of the class should initialize $l$, $b$, and $h$ to $0$. 

The parameterized constructor *Box(int length, int breadth, int height)* should initialize *Box*'s $l, b$ and $h$ to length, breadth and height.

The copy constructor *Box*$($*Box* $B$) should set $l, b$ and $h$ to $B$'s $l, b$ and $h$, respectively. 

Apart from the above, the class should have $4$ functions:  

- *int getLength()*  - Return box's length  
- *int getBreadth()* - Return box's breadth  
- *int getHeight()*  - Return box's height    
- *long long CalculateVolume()* - Return the volume of the box

Overload the operator $<$ for the class *Box*. *Box* $A$ $<$ *Box* $B$  if:

1. $A.l$ < $B.l$  
2. $A.b$ < $B.b$ and $A.l$==$B.l$  
3. $A.h$ < $B.h$ and $A.b$==$B.b$ and $A.l$==$B.l$  

Overload operator $<<$ for the class *Box()*.  
If $B$ is an object of class *Box*:

$cout<<B$ should print $B.l$, $B.b$ and $B.h$ on a single line separated by spaces.

For example,
```cpp
Box b1; // Should set b1.l = b1.b = b1.h = 0;
Box b2(2, 3, 4); // Should set b1.l = 2, b1.b = 3, b1.h = 4;
b2.getLength();	// Should return 2
b2.getBreadth(); // Should return 3
b2.getheight();	// Should return 4
b2.CalculateVolume(); // Should return 24
bool x = (b1 < b2);	// Should return true based on the conditions given
cout<<b2; // Should print 2 3 4 in order.
```

**Input Format**




**Constraints**

   
$0 \le l,b,h \le 10^5$  
Two boxes being compared using the $<$ operator will not have all three dimensions equal.

**Output Format**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T07:48:43.579Z  

```cpp

class Box {
    int l, b, h;
public:
    Box() : l(0), b(0), h(0) {}
    Box(int length, int breadth, int height) : l(length), b(breadth), h(height) {}
    Box(const Box& B) : l(B.l), b(B.b), h(B.h) {}

    int getLength() { return l; }
    int getBreadth() { return b; }
    int getHeight() { return h; }
    long long CalculateVolume() { return (long long)l * b * h; }

    bool operator<(Box& B) {
        if (l < B.l) return true;
        if (b < B.b && l == B.l) return true;
        if (h < B.h && b == B.b && l == B.l) return true;
        return false;
    }

    friend ostream& operator<<(ostream& out, Box& B) {
        out << B.l << " " << B.b << " " << B.h;
        return out;
    }
};

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/box-it/problem)