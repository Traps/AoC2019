from math import floor

input_file = open('D01/.input', 'r')

input_text = input_file.read()

input_file.close()

module_masses = [int(m_string) for m_string in input_text.splitlines()]

fuel_sum = 0
for mass in module_masses:
    fuel_needed = floor(mass / 3) - 2

    if fuel_needed > 0:
        fuel_sum += fuel_needed

        module_masses.append(fuel_needed)

print('Fuel needed:', fuel_sum)