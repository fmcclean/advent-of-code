with open('input2.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    max_counts = {"red": 0, "green": 0, "blue": 0}
    game_id, game = line.split(': ')
    cube_sets = game.split('; ')
    for cube_set in cube_sets:
        cubes = cube_set.split(', ')
        for cube in cubes:
            count, colour = cube.split(' ')
            if max_counts[colour.strip()] < int(count):
                max_counts[colour.strip()] = int(count)

    total += max_counts['red'] * max_counts['green'] * max_counts['blue']

print(total)