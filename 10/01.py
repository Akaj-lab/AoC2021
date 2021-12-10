with open("10/input.txt", "r") as f:
    f = f.read().split()
    posibly_corrupted = []
    pts = 0

    for i in f:
        y = [a for a in i]
        for dyjfdjfdj in range(1000):
            for j in range(1, len(y)+1):
                try:
                    if y[j-1] == '(' and y[j] == ')':
                        y.pop(j)
                        y.pop(j-1)
                    elif y[j-1] == '[' and y[j] == ']':
                        y.pop(j)
                        y.pop(j-1)
                    elif y[j-1] == '{' and y[j] == '}':
                        y.pop(j)
                        y.pop(j-1)
                    elif y[j-1] == '<' and y[j] == '>':
                        y.pop(j)
                        y.pop(j-1)
                except IndexError:
                    continue

        ind = len(y)-1
        for k in [')', ']', '}', '>']:
            try:
                if y.index(k) < ind:
                    ind = y.index(k)
            except ValueError:
                continue
        if y[ind] == ')':
            pts += 3
        elif y[ind] == ']':
            pts += 57
        elif y[ind] == '}':
            pts += 1197
        elif y[ind] == '>':
            pts += 25137

        print(y)

        print(pts)
        pass
