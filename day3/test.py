with open('input.txt') as f:
    lines = f.readlines()


gen = 0
a = []
for i in range (0, len(lines)):
#for i in range (0, 2):
    if lines[i][12] == "1":
        gen += 1

# if gen > 500:
#     a.append(1)

print(gen)
