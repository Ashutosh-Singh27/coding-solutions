t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = 21 - a - b
    print(c if 1 <= c <= 10 else -1)