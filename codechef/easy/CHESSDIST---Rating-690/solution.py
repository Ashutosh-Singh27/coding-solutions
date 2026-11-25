# cook your dish here
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x1, y1, x2, y2 = map(int, data[idx:idx + 4])
        idx += 4
        out.append(str(max(abs(x1 - x2), abs(y1 - y2))))
    print("\n".join(out))

main()