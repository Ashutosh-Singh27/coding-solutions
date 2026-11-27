# cook your dish here
t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    print("Alice" if ((p + q) // 2) % 2 == 0 else "Bob")