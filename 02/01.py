with open("input.txt", "r") as f:
    f = f.read().split("\n")
    down = 0
    up = 0
    fw = 0
    for i in f:
        if i[0] == 'u':
            up += int(i[-1])
        elif i[0] == 'd':
            down += int(i[-1])
        elif i[0] == 'f':
            fw += int(i[-1])
        else:
            raise "idk what could go wrong"

    print(str(down) + ' ' + str(up) + ' ' + str(fw) +
          ' ' + str(down-up) + ' ' + str((down-up)*fw))
