# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print(((n + 5) // 6) * x)