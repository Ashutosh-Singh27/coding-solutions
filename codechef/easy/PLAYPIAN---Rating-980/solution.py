# cook your dish here
t = int(input())
for _ in range(t):
    s = input().strip()
    valid = True
    for i in range(0, len(s), 2):
        if s[i] == s[i + 1]:
            valid = False
            break
    print("yes" if valid else "no")