with open('input5.txt') as f:
    steps = f.read().split('\n\n')

seeds = steps.pop(0).split(': ')[1].split()
locations = []

for seed in seeds:
    n = int(seed)
    for i, step in enumerate(steps):
        for line in step.split('\n')[1:]:
            dest, src, length = [int(n) for n in line.split()]
            if n >= src and n < src + length:
                n = dest + n - src
                break

    locations.append(n)
    
print(min(locations))