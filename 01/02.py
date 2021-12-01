f = open("input.txt", 'r').read()
f = f.split("\n")

g = open("output.txt", "w")

last = 0
count = 0

for i in range(2, len(f)):
    curr = int(f[i-2]) + int(f[i-1]) + int(f[i])
    if last == 0:
        pass
    elif last < curr:
        count += 1
    last = curr

print("done")
print(count)
