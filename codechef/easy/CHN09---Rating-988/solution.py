# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    a=s.count('a')
    b=len(s)-a
    print(min(a,b))