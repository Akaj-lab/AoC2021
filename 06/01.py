with open("input.txt", "r") as f:
    f = f.read().split(",")
    a = []
    for i in f:
        a.append(int(i))
    for day in range(80):
        for i in range(len(a)):
            if int(a[i]) == 0:
                a.append(8)
                a[i] = 7
            a[i] -= 1

    print(len(a))
