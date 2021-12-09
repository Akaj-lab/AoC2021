with open("input.txt", "r") as f:
    f = f.read().split("\n")
    a = []
    for i in f:
        b = []
        for j in i:
            b.append(int(j))
        a.append(b)
    sum = 0
    for i in range(1, 101):
        for j in range(1, 101):
            abc = a[i][j]
            if a[i][j] == 9:
                pass
            else:
                one = abc < a[i-1][j]
                two = abc < a[i+1][j]
                three = abc < a[i][j-1]
                four = abc < a[i][j+1]
                if one + two + three + four == 4:
                    sum += abc + 1
    print(sum)
