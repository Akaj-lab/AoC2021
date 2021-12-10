import numpy as np
with open("10/input.txt", "r") as f:
    f = f.read().split()
    pts = 0
    incomplete = []
    scores = []
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
        else:
            y.reverse()
            score = 0
            for j in y:
                cur = 0
                if j == '(':
                    cur = 1
                elif j == '[':
                    cur = 2
                elif j == '{':
                    cur = 3
                elif j == '<':
                    cur = 4
                score = score*5 + cur
            incomplete.append(y)
            scores.append(score)

    a_list = []
    for i in incomplete:
        a_str = ''
        for j in i:
            a_str += j
            print(j, end='')
        a_list.append(a_str)
        print()
    print(np.median(scores))
