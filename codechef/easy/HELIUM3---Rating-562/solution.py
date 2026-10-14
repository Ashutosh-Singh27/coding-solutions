# cook your dish here
t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    print("Yes" if x * y >= a * b else "No")