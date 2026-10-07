# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print("YES" if 2 * z > x * y else "NO")