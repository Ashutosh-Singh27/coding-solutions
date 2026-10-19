# cook your dish here
import sys

data = sys.stdin.read().split()
t = int(data[0])
idx = 1
for _ in range(t):
    a, b, c, d = map(int, data[idx:idx + 4])
    idx += 4
    if c >= a and d >= b:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")