# Say "Hello, World!" With C++

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

**Objective**		
This is a simple challenge to help you practice printing to [stdout](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29). You may also want to complete [Solve Me First](https://www.hackerrank.com/challenges/solve-me-first) in C++ before attempting this challenge.  

---- 

We're starting out by printing the most famous computing phrase of all time! In the editor below, use either [printf](http://www.cplusplus.com/printf) or [cout](http://www.cplusplus.com/cout) to print the string $\texttt{Hello, World!}$ to [stdout](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29).  

The more popular command form is `cout`.  It has the following basic form:  

`cout<<value_to_print<<value_to_print;`  

Any number of values can be printed using one command as shown.  

The `printf` command comes from C language.  It accepts an optional format specification and a list of variables.  Two examples for printing a string are:  

`printf("%s", string);`
`printf(string);`  

Note that neither method adds a newline.  It only prints what you tell it to.  

**Input Format**

 

**Constraints**

 

**Output Format**

Print $\texttt{Hello, World!}$ to stdout.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T06:15:22.044Z  

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    printf("Hello, World!");
    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/cpp-hello-world/problem)