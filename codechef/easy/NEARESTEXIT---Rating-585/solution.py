# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    if x - 1 < 100 - x:
        print("LEFT")
    else:
        print("RIGHT")