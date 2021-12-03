def most_common_bit(list, pos):
    ones = 0
    zeros = 0
    for i in list:
        if(int(i[pos])):
            ones += 1
        else:
            zeros += 1
    return 1 if ones >= zeros else 0
    return 0 if ones >= zeros else 1  # comment first line to make least common bit


with open("03/input.txt", "r") as f:
    f = f.read().split("\n")
    g = f
    i = 0
    while(len(g) > 1):
        mcb = str(most_common_bit(g, i))
        torem = []
        for j in g:
            if j[i] != mcb:
                torem.append(j)
        i += 1
        print(g)
        for j in torem:
            g.remove(j)
    print(g)
