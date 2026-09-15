# cook your dish here
T = int(input())

for _ in range(T):
    X = int(input())
    S = input()

    carlsen = 0
    chef = 0

    for game in S:
        if game == 'C':
            carlsen += 2
        elif game == 'N':
            chef += 2
        else:
            carlsen += 1
            chef += 1

    if carlsen > chef:
        print(60 * X)
    elif carlsen == chef:
        print(55 * X)
    else:
        print(40 * X)