# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if 2 * y >= x else "NO")