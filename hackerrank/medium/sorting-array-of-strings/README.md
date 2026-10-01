# Sorting Array of Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

To sort a given array of strings into lexicographically increasing order or into an order in which the string with the lowest length appears first, a sorting function with a flag indicating the type of comparison strategy can be written. The disadvantage with doing so is having to rewrite the function for every new comparison strategy. 

A better implementation would be to write a sorting function that accepts a pointer to the function that compares each pair of strings. Doing this will mean only passing a pointer to the sorting function with every new comparison strategy.

---
 
<!-- We could make a sorting function and pass the function a flag telling it which comparison strategy to use, but that would mean that whenever we invented a new comparison strategy, we would have to define a new code or flag value and rewrite the sorting function.   
But, if we observe that the final ordering depends entirely on the behaviour of the comparison function, a better implementation would be if we write our sorting function to accept a pointer to the function which we want it to use to compare each pair of strings.   
Making it sort in a different order, according to a different comparison strategy, will then not require rewriting sorting at all, but instead will just involve passing it a pointer to a different comparison function. --> 

Given an array of strings, you need to implement a $\texttt{string_sort}$ function which sorts the strings according to a comparison function, i.e, you need to implement the function :  
```
void string_sort(const char **arr,const int cnt, int (*cmp_func)(const char* a, const char* b)){
    
}
```
The arguments passed to this function are:   

- an array of strings : ${arr}$  
- length of string array: ${count}$  
- pointer to the string comparison function: $cmp\_func$  

You also need to implement the following four string comparison functions:  

1. $\texttt{int lexicographic_sort(char*, char*)}$ to sort the strings in lexicographically non-decreasing order.

2. $\texttt{int lexicographic_sort_reverse(char*, char*)}$ to sort the strings in lexicographically non-increasing order.

3. $\texttt{int sort_by_number_of_distinct_characters(char*, char*)}$ to sort the strings in non-decreasing order of the number of distinct characters present in them. If two strings have the same number of distinct characters present in them, then the lexicographically smaller string should appear first.

4. $\texttt{int sort_by_length(char*, char*)}$ to sort the strings in non-decreasing order of their lengths. If two strings have the same length, then the lexicographically smaller string should appear first.

**Input Format**

You just need to complete the function `string\_sort` and implement the four string comparison functions.   

**Constraints**

- $1 \enspace \le \enspace $ No. of Strings $ \enspace \le \enspace 50 $  
- $1 \enspace \le \enspace $ Total Length of all the strings $ \enspace \le \enspace 2500 $  
- You have to write your own sorting function and you cannot use the inbuilt $qsort$ function  
- The strings consists of lower-case English Alphabets only.  

**Output Format**

The locked code-stub will check the logic of your code. The output consists of the strings sorted according to the four comparsion functions in the order mentioned in the problem statement.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T16:00:49.317Z  

```c

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

int count_distinct(const char* s) {
    int seen[26] = {0};
    int count = 0;
    for (; *s; s++) {
        if (!seen[*s - 'a']) {
            seen[*s - 'a'] = 1;
            count++;
        }
    }
    return count;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int da = count_distinct(a);
    int db = count_distinct(b);
    if (da != db) return da - db;
    return strcmp(a, b);
}

int sort_by_length(const char* a, const char* b) {
    int la = strlen(a);
    int lb = strlen(b);
    if (la != lb) return la - lb;
    return strcmp(a, b);
}

void string_sort(char** arr, const int len, int (*cmp_func)(const char* a, const char* b)) {
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - i - 1; j++) {
            if (cmp_func(arr[j], arr[j + 1]) > 0) {
                char* tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sorting-array-of-strings/problem)