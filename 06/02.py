with open("input.txt", "r") as f:
    f = f.read().split(",")
    a = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in f:
        a[int(i)] += 1
    for day in range(257):
        b = a.copy()
        a[0] = b[1]
        a[1] = b[2]
        a[2] = b[3]
        a[3] = b[4]
        a[4] = b[5]
        a[5] = b[6]
        a[6] = b[7] + b[0]
        a[7] = b[8]
        a[8] = b[0]
        print(day)
    sum = 0
    for i in range(8):
        sum += a[i]
    print(sum)
