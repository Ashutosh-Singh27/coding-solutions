# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print("YES" if x % n == 0 else "NO")