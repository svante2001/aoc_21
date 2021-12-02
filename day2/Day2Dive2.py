with open('input.txt') as f:
    lines = f.readlines()

d = 0
p = 0
aim = 0
for i in range(0, len(lines)):
    if lines[i][0] == "f":
        p += int(lines[i][8])
        d += aim * int(lines[i][8])
    elif lines[i][0] == "d":
        #d += int(lines[i][5])
        aim += int(lines[i][5])
    elif lines[i][0] == "u":
        #d -= int(lines[i][3])
        aim -= int(lines[i][3])

print("{}" .format(d*p))