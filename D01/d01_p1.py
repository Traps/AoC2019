from math import floor

input_file = open('D01/.input', 'r')

input_text = input_file.read()

input_file.close()

module_masses = [int(m_string) for m_string in input_text.splitlines()]

fuel_sum = sum([floor(mass / 3) - 2 for mass in module_masses])

print('Fuel needed:', fuel_sum)
