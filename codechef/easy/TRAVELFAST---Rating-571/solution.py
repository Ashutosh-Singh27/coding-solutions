# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x < y:
        print("BIKE")
    elif x > y:
        print("CAR")
    else:
        print("SAME")