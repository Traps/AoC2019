input_file = open('D02/.input', 'r')

input_text = input_file.read()

input_file.close()

program = [int(s) for s in input_text.split(',')]

program[1:3] = [12, 2]

for i_position in range(0, len(program), 4):
    op, i_r1, i_r2, i_w = program[i_position:(i_position+4)]

    if op == 99:
        break

    elif op == 1:
        program[i_w] = program[i_r1] + program[i_r2]

    elif op == 2:
        program[i_w] = program[i_r1] * program[i_r2]

print('Program output:',program[0])