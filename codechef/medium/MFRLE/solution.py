# cook your dish here
s = input()

count = {}
for ch in s:
    if ch.isalpha():
        ch = ch.lower()
        count[ch] = count.get(ch, 0) + 1

best = None
best_count = -1
for letter in sorted(count.keys()):
    if count[letter] > best_count:
        best_count = count[letter]
        best = letter

print(best)