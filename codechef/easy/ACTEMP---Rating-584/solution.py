# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print("Yes" if max(a, c) <= b else "No")