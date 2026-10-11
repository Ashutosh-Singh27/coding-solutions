# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print((n * x + 3) // 4)