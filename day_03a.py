with open("input3.txt") as f:
    lines = f.readlines()

numbers = []

for i, line in enumerate(lines):
    line = line.strip()
    number = ''
    part = False
    for j, char in enumerate(line):
        if char.isdigit():
            number += char
            upper, center, lower = max(0,i-1), i, min(len(lines)-1,i+1)
            left, middle, right = max(0,j-1), j, min(len(line)-1,j+1)
            neighbours = [
                lines[upper][left],
                lines[upper][middle],
                lines[upper][right],
                lines[center][left],
                lines[center][right],
                lines[lower][left],
                lines[lower][middle],
                lines[lower][right]
                ]
            for neighbour in neighbours:
                if not (neighbour.isdigit() or neighbour == '.'):
                    part = True
                    break
        if (j == len(line) - 1 or not char.isdigit()) and len(number) > 0:
            if part:
                numbers.append(int(number))
            number = ''
            part = False

print(sum(numbers))
# 607509 is too high
# 506536 is too low