# cook your dish here
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    first = a * 10
    second = b * 5
    if first == second:
        print("ANY")
    elif first > second:
        print("FIRST")
    else:
        print("SECOND")