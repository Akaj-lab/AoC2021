import numpy


def factorial_sum(x):
    o = 0
    for i in range(x+1):
        o += i
    return o


with open("input.txt", "r") as f:
    f = f.read().split(",")
    sum = 0
    a = []
    for i in f:
        a.append(int(i))
    # zaradi specifičnega inpute, more zavkrožit navzgor
    avg = numpy.average(a)
    print(avg)
    fuel = 0
    for i in a:
        fuel += factorial_sum(abs(avg-i))
    print(fuel)
