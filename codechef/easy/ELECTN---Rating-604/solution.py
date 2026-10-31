# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for v in a if v >= x))