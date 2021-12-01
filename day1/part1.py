with open('input.txt') as f:
    lines = f.readlines()
    
c = 0
for i in range (0, len(lines)):
    if i != len(lines):        
        if lines[i-1] < lines[i]:
            c += 1
print(c+1)