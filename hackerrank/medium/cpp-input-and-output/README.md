# Input and Output

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Objective**		
In this challenge, we practice reading input from stdin and printing output to stdout. 

----

In C++, you can read a single whitespace-separated token of input using [cin](http://www.cplusplus.com/cin), and print output to stdout using [cout](http://www.cplusplus.com/printf). For example, let's say we declare the following variables:

```cpp
string s;
int n;
```
and we want to use *cin* to read the input "High 5" from stdin. We can do this with the following code:

```cpp
cin >> s >> n;
```

This reads the first word ("High") from stdin and saves it as string $s$, then reads the second word ("$5$") from stdin and saves it as integer $n$. If we want to print these values to stdout, separated by a space, we write the following code:

```cpp
cout << s << " " << n << endl;
```

This code prints the contents of string $s$, a single space ($\text{" "}$), then the integer $n$. We end our line of output with a newline using [endl](http://www.cplusplus.com/endl). This results in the following output:

	High 5
	


**Task**	
Read $3$ numbers from stdin and print their sum to stdout.


**Input Format**

One line that contains $3$ space-separated integers: $a$, $b$, and $c$.  



**Constraints**

- $1 \le a, b, c \le 1000$ 

**Output Format**

Print the sum of the three numbers on a single line.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T16:39:35.350Z  

```cpp
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << a + b + c << endl;
    /*bv Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/cpp-input-and-output/problem)