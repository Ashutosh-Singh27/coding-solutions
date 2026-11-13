t = int(input())
for _ in range(t):
    x = int(input())
    r = x % 3
    if r == 0:
        print("NORMAL")
    elif r == 1:
        print("HUGE")
    else:
        print("SMALL")