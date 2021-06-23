for _ in range(int(input())):
# for _ in range(1):
    s = int(input())
    # s = 8735373
    fives = 0
    twos = 0

    # for i in range(2, s + 1):
    #     j = i
    #     while j % 5 == 0 and j > 0:
    #         fives += 1
    #         j /= 5
    #     while j % 2 == 0 and twos < fives and j > 0:
    #         twos += 1
    #         j /= 2

    s5 = s
    s5 = int(s5 / 5)
    while s5 > 0:
        fives += s5
        s5 = int(s5 / 5)

    s2 = s
    s2 = int(s2 / 2)
    while s2 > 0:
        twos += s2
        if twos > fives:
            break
        s2 = int(s2 / 2)

    print(min(fives, twos))
