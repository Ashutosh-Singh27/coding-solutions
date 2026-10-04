# Conditional Statements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_if_ and _else_ are two of the most frequently used conditionals in C/C++, and they enable you to execute zero or one conditional statement among many such dependent conditional statements. We use them in the following ways:

1. *if:* This executes the body of bracketed code starting with $statement1$ if $condition$ evaluates to *true*.
	
    	if (condition) {
        	statement1;
            ...
        }

2. *if - else:* This executes the body of bracketed code starting with $statement1$ if $condition$ evaluates to *true*, or it executes the body of code starting with $statement2$ if $condition$ evaluates to *false*. Note that only *one* of the bracketed code sections will ever be executed.

		if (condition) {
        	statement1;
            ...
        }
        else {
            statement2;
        	...
        }

3. *if - else if - else:* In this structure, dependent statements are chained together and the $condition$ for each statement is only checked if all prior conditions in the chain evaluated to *false*. Once a $condition$ evaluates to *true*, the bracketed code associated with that statement is executed and the program then skips to the end of the chain of statements and continues executing. If each $condition$ in the chain evaluates to false, then the body of bracketed code in the *else* block at the end is executed.

		if(first condition) {
        	...
        }
        else if(second condition) {
        	...
        }
        .
        .
        .
        else if((n-1)'th condition) {
            ....
        }
        else {
        	...
        }
        
---

Given a positive integer $n$, do the following:

- If $1 \le n \le 9$, print the lowercase English word corresponding to the number (e.g., `one` for $1$, `two` for $2$, etc.).
- If $n \gt 9$, print `Greater than 9`.

**Input Format**

A single integer, $n$.

**Constraints**

- $1 \le n \le 10^9$

**Output Format**

If $1 \le n \le 9$, then print the lowercase English word corresponding to the number (e.g., `one` for $1$, `two` for $2$, etc.); otherwise, print `Greater than 9`.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-04T15:06:44.038Z  

```cpp
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    if (n == 1) {
        cout << "one" << endl;
    } else if (n == 2) {
        cout << "two" << endl;
    } else if (n == 3) {
        cout << "three" << endl;
    } else if (n == 4) {
        cout << "four" << endl;
    } else if (n == 5) {
        cout << "five" << endl;
    } else if (n == 6) {
        cout << "six" << endl;
    } else if (n == 7) {
        cout << "seven" << endl;
    } else if (n == 8) {
        cout << "eight" << endl;
    } else if (n == 9) {
        cout << "nine" << endl;
    } else {
        cout << "Greater than 9" << endl;
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem)