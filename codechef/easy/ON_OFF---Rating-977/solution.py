t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    r = input().strip()
    diff = sum(1 for a, b in zip(s, r) if a != b)
    print(1 if diff % 2 == 0 else 0)