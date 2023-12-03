with open('input2.txt') as f:
    lines = f.readlines()

counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total = 0

for line in lines:
    possible = True
    game_id, game = line.split(': ')
    cube_sets = game.split('; ')
    for cube_set in cube_sets:
        cubes = cube_set.split(', ')
        for cube in cubes:
            count, colour = cube.split(' ')
            if counts[colour.strip()] < int(count):
                possible = False
    
    if possible:
        total += int(game_id[5:])

print(total)