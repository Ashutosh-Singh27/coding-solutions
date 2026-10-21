# cook your dish here
T = int(input())
for _ in range(T):
    p, q, r, s = map(int, input().split())
    total = p + q + r + s
    if max(p, q, r, s) > total - max(p, q, r, s):
        print("YES")
    else:
        print("NO")