# cook your dish here
t = int(input())
for _ in range(t):
    s = input().strip()
    print("Good" if "010" in s or "101" in s else "Bad")