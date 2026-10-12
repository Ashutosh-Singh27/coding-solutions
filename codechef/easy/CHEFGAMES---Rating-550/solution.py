# cook your dish here
t = int(input())
for _ in range(t):
    r = input().split()
    if len(r) == 1:
        r = list(r[0])
    print("IN" if all(x == "0" for x in r) else "OUT")