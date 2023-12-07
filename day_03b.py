with open("input3.txt") as f:
    lines = f.readlines()

numbers = []
number_idx = []
idx = 0


for line in lines:
    line_idx = []
    number = ''
    for i, char in enumerate(line):
        if char.isdigit():
            number += char
            line_idx.append(idx)
        else:
            line_idx.append(-1)
        
        if len(number) > 0 and (not char.isdigit() or i == len(line)-1):
            numbers.append(int(number))
            number = ''
            
            idx += 1
        
    number_idx.append(line_idx)

total = 0

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '*':
            upper, center, lower = max(0,i-1), i, min(len(lines)-1,i+1)
            left, middle, right = max(0,j-1), j, min(len(line)-1,j+1)
            neighbours = [
                number_idx[upper][left],
                number_idx[upper][middle],
                number_idx[upper][right],
                number_idx[center][left],
                number_idx[center][right],
                number_idx[lower][left],
                number_idx[lower][middle],
                number_idx[lower][right]
                ]
            neighbours = list(set([n for n in neighbours if n != -1]))
            if len(neighbours) == 2:
                total += numbers[neighbours[0]] * numbers[neighbours[1]]

print(total)
# 612377 is too low
# 3666384 is too low