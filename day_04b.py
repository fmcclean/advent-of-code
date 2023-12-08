with open('input4.txt') as f:
    lines = f.readlines()

cards = [1 for _ in range(len(lines))]

for i, line in enumerate(lines):
    line = line.strip()
    _, line = line.split(':')
    winning, have = line.split('|')
    matches = len([n for n in have.split() if n in winning.split()])
    for j in range(matches):
        cards[i+j+1] += cards[i]
    
print(sum(cards))
    

# 3559 is too low
# 3560 is too low