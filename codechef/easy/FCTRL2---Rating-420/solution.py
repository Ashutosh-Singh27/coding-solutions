# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)