# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(1 for x in arr if x >= 1000))