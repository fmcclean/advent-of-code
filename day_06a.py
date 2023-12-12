with open('input6.txt') as f:
    times, distances = [l.split()[1:] for l in f.readlines()]

answer = 1

for time, distance in zip(times, distances):
    ways = []
    for t in range(1, int(time)):
        if t * (int(time)-t) > int(distance):
            ways.append(t)
    answer *= len(ways)

print(answer)