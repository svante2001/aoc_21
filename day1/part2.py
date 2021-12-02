with open('input.txt') as f:
    lines = f.readlines()

sums = []
i = 0
while i < len(lines)-1:
    sums.append((int(lines[i-1]) + int(lines[i]) + int(lines[i+1])))
    i += 1
    
c = 0
for i in range (0, len(sums)):
    if sums[i-1] < sums[i]:
        c += 1

print(c)