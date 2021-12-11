import numpy as np
with open("11/input.txt", "r") as f:
    f = f.read().split()
    a = []
    for i in f:
        b = []
        for j in i:
            b.append(int(j))
        a.append(b)
    full_grid = []
    for i in range(10):
        for j in range(10):
            full_grid.append((i, j))
    total_flashes = 0
    a = np.array(a)
    step = 0
    while True:
        step += 1
        flashed = []
        last = np.array([])
        while(not(np.array_equal(last, a))):
            last = a.copy()
            for j in range(10):
                for k in range(10):
                    if a[j][k] >= 9 and not((j, k) in flashed):
                        flashed.append((j, k))
                        for x in [-1, 0, 1]:
                            for y in [-1, 0, 1]:
                                try:
                                    if(j-x < 0 or k-y < 0):
                                        raise ValueError
                                    a[j-x][k-y] += 1
                                except:
                                    pass
                        total_flashes += 1
        a = a + 1
        loob = True
        for i in full_grid:
            if not i in flashed:
                loob = False
        if loob:
            print(step)
            break
        for j, k in flashed:
            a[j][k] = 0
    print(total_flashes)
