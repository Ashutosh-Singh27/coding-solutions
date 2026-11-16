# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    table = str.maketrans("ATCG", "TAGC")
    print(s.translate(table))