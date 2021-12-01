f = open("input.txt", 'r').read()
f = f.split("\n")

g = open("output.txt", "w")

last = 0
count = 0

for i in f:
    if last == 0:
        pass
    elif last < i:
        g.write(i + " increase\n")
        count += 1
    else:
        g.write(i + " decrease\n")
    last = i

print("done")
print(count)
