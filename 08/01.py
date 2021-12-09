with open("input1.txt", "r") as f:
    f = f.read().split("\n")
    sum = 0
    for i in f:
        i = i.split(" ")
        for j in i:
            if len(j) in [2, 4, 3, 7]:
                # print(j)
                # print(len(j))
                sum += 1
    print(sum)
