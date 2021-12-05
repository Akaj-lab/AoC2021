with open("input.txt", "r") as f:
    f = f.read().split("\n")
    map = []
    for i in range(0, 1000):
        list = []
        for j in range(0, 1000):
            list.append(0)
        map.append(list)
    for i in f:
        i = i.split(" -> ")
        x1 = int(i[0].split(",")[0])
        y1 = int(i[0].split(",")[1])
        x2 = int(i[1].split(",")[0])
        y2 = int(i[1].split(",")[1])
        if x1 == x2:
            print(F'{x1},{y1} -> {x2},{y2}  x')
            y1_cp = y1
            y1, y2 = (y1, y2) if y1 < y2 else (y2, y1_cp)
            for j in range(y1, y2+1):
                map[j][x1] += 1
        elif y1 == y2:
            print(F'{x1},{y1} -> {x2},{y2}  y')
            x1_cp = x1
            x1, x2 = (x1, x2) if x1 < x2 else (x2, x1_cp)
            for j in range(x1, x2+1):
                map[y1][j] += 1

        elif x1 < x2 and y1 < y2:  # \
            for j in range(0, x2 - x1 + 1):
                map[y1 + j][x1 + j] += 1
        elif x1 > x2 and y1 > y2:  # \
            for j in range(0, x1-x2+1):
                map[y1 - j][x1 - j] += 1

        elif x1 < x2 and y1 > y2:  # /
            for j in range(0, x2 - x1 + 1):
                map[y1-j][x1+j] += 1
        elif x1 > x2 and y1 < y2:  # /
            for j in range(0, x1 - x2 + 1):
                map[y1+j][x1-j] += 1
    print(map)
    count = 0
    cnt = 0
    for i in map:
        for j in i:
            print(str(j) + ' ', end='')
            if j >= 2:
                count += 1
            else:
                cnt += 1
        print()
    print(count, cnt)
