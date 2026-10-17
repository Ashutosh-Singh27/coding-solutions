# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    d = max(0, n - x)
    print((d + 3) // 4)