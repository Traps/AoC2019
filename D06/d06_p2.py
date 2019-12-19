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

for planet in path1[::-1]:
    if planet in path2:
        print(planet)
        break

n_steps = len(path1) + len(path2) - len(set(path1 + path2)) - 2
print(n_steps)

print(len(path1),len(set(path1)))
print(len(path2))
print(path1.index(planet))
print(path2.index(planet))
print(len(set(path1 + path2)))