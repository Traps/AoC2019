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

n_orbits = sum(len(rs) - 1 for rs in resolved_structures)

print('Total number of orbits:', n_orbits)
