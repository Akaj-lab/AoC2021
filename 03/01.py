with open("input.txt", "r") as f:
    f = f.read().split("\n")
    ones = [0]*12
    zeros = [0]*12
    for i in f:
        for j in range(0, 12):
            if(int(i[j])):
                ones[j] += 1
            else:
                zeros[j] += 1
    out = ''
    for i in range(len(zeros)):
        if ones[i] > zeros[i]:
            out += '1'
        else:
            out += '0'

    print(out)
