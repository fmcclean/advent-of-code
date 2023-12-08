with open('input4.txt') as f:
    lines = f.readlines()

points_total = 0
for line in lines:
    line = line.strip()
    _, line = line.split(':')
    winning, have = line.split('|')
    points = 0
    for number in have.split(' '):
        if number in winning.split():
            if points == 0:
                points = 1
            else:
                points *= 2
    points_total += points

print(points_total)

# 321035 is too high