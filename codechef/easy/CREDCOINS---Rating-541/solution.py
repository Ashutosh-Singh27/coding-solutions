# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if [a, b, c].count(0) >= 2:
        print("Water filling time")
    else:
        print("Not now")