# Dynamic Array in C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Snow Howler is the librarian at the central library of the city of HuskyLand.  He must handle requests which come in the following forms:  

*1 x y* : Insert a book with $y$ pages at the end of the $x^{th}$ shelf.  

*2 x y* : Print the number of pages in the $y^{th}$ book on the $x^{th}$ shelf.     

*3 x* : Print the number of books on the $x^{th}$ shelf.  

Snow Howler has got an assistant, Oshie, provided by the Department of Education.  Although inexperienced, Oshie can handle all of the queries of types *2* and *3*.  

Help Snow Howler deal with all the queries of type *1*.  

Oshie has used two arrays:  

```c
int* total_number_of_books;
/*
 * This stores the total number of books on each shelf.
 */

int** total_number_of_pages;
/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
```

**Input Format**

The first line contains an integer $total\_number\_of\_shelves$, the number of shelves in the library.  
The second line contains an integer $total\_number\_of\_queries$, the number of requests.  
Each of the following $total\_number\_of\_queries$ lines contains a request in one of the three specified formats.  

**Constraints**

- $1 \le \enspace total\_number\_of\_shelves \enspace \le 10^5$  
- $1 \le \enspace total\_number\_of\_queries \enspace \le 10^5$  
- For each query of the second type, it is guaranteed that a book is present on the $x^{th}$ shelf at $y^{th}$ index.  
- $0 \le \enspace x \enspace < total\_number\_of\_shelves$  
- Both the shelves and the books are numbered starting from 0.
- Maximum number of books per shelf $\leq 1100$.

**Output Format**

Write the logic for the requests of type 1.  The logic for requests of types 2 and 3 are provided.

## Solution

**Language:** C  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T13:57:19.168Z  

```c

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);

    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);

    total_number_of_books = calloc(total_number_of_shelves, sizeof(int));
    total_number_of_pages = calloc(total_number_of_shelves, sizeof(int*));

    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);

        if (type_of_query == 1) {
            int x, y;
            scanf("%d %d", &x, &y);
            total_number_of_books[x]++;
            total_number_of_pages[x] = realloc(
                total_number_of_pages[x],
                total_number_of_books[x] * sizeof(int)
            );
            total_number_of_pages[x][total_number_of_books[x] - 1] = y;


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/dynamic-array-in-c/problem)