input_file = open('D06/.input', 'r')

input_lines = input_file.read().splitlines()

input_file.close()

orbit_pairs = [line.split(')') for line in input_lines]

resolved_structures = []

for pair in orbit_pairs:
    if 'COM' in pair:
        resolved_structures.append(pair)
        orbit_pairs.remove(pair)

while len(orbit_pairs) > 0:
    for rs in resolved_structures:
        for pair in orbit_pairs:
            if rs[-1] == pair[0]:
                resolved_structures.append(rs + [pair[1]])
                orbit_pairs.remove(pair)

start = 'YOU'
goal = 'SAN'

path1 = []
path2 = []

for rs in resolved_structures:
    if rs[-1] == start:
        path1 = rs
    
    elif rs[-1] == goal:
        path2 = rs

part1 = [p for p in path1 if p not in path2]
part2 = [p for p in path2 if p not in path1]

print('Number of orbit transfers from YOU to SAN:', len(part1) + len(part2) - 2)