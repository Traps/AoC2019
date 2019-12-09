def run_intcode(intcode):
    for i_pointer in range(0, len(intcode), 4):
        op, i_r1, i_r2, i_w = intcode[i_pointer:(i_pointer+4)]

        if op == 99:
            return intcode[0]

        elif op == 1:
            intcode[i_w] = intcode[i_r1] + intcode[i_r2]

        elif op == 2:
            intcode[i_w] = intcode[i_r1] * intcode[i_r2]

        else:
            return -1

    return -1

target_output = 19690720

input_file = open('D02/.input', 'r')

input_text = input_file.read()

input_file.close()

program = [int(s) for s in input_text.split(',')]

test_pairs = [[noun, verb] for noun in range(0,100) for verb in range(0,100)]

for pair in test_pairs:
    program[1:3] = pair

    if run_intcode(program.copy()) == target_output:
        print('Answer:', 100 * pair[0] + pair[1])
        break
