# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print(max(0, z - y // x))