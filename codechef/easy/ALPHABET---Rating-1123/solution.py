# cook your dish here
s = set(input())
n= int(input())
for _ in range(n):
    w= input()
    print("Yes"if set(w).issubset(s) else "No")