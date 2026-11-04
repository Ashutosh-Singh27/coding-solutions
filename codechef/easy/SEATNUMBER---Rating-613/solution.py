# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    deck = "Lower" if n <= 15 else "Upper"
    kind = "Double" if (n <= 10 or 16 <= n <= 25) else "Single"
    print(deck, kind)