with open('input.txt') as f:
    lines = f.readlines()

g = []
e = []

#for i in range (0, len(lines)):
for i in range (0, 4):
    if i != len(lines):
        sumt = []
        for j in range (0, 12):
            sumt.append(lines[i][j])

        s = 0
        for i in range(0, len(sumt)):    
            s = s + int(sumt[i])

        if s > 6:
            g.append(1)
            e.append(0)
        else:
            g.append(0)
            e.append(1)

print("g: {}"  .format(g))
print("e: {}"  .format(e))


resG = int("".join(str(x) for x in g), 2)
resE = int("".join(str(x) for x in e), 2)
print("g: {}" .format(resG))
print("e: {}" .format(resE))
print("m: {}" .format(resG * resE))