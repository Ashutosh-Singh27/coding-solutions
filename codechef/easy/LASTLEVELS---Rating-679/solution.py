# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    print(x * y + ((x - 1) // 3) * z)