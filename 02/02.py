with open("input.txt", "r") as f:
    f = f.read().split("\n")
    dep = 0
    fw = 0
    aim = 0
    for i in f:
        if i[0] == 'u':
            aim += -int(i[-1])
        elif i[0] == 'd':
            aim += int(i[-1])
        elif i[0] == 'f':
            x = int(i[-1])
            fw += x
            dep += x*aim
        else:
            raise "idk what could go wrong"

    print(str(dep) + ' ' + str(aim) + ' ' + str(fw) +
          ' ' + str(dep*fw))
