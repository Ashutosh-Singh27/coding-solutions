# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    words = s.split()
    result = []
    for word in words:
        if word.isupper():
            result.append(word)
        else:
            result.append(word[0].upper() + word[1:].lower())
    print(' '.join(result))