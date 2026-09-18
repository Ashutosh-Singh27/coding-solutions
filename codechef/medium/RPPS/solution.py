# cook your dish here
s = input().strip()

count = {}
for i in range(len(s) - 1):
    pair = s[i:i+2]
    count[pair] = count.get(pair, 0) + 1

result = sum(1 for v in count.values() if v > 1)
print(result)