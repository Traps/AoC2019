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

input_file = open('D02/.input', 'r')

input_text = input_file.read()

input_file.close()

program = [int(s) for s in input_text.split(',')]

program[1:3] = [12, 2]

print('Program output:', run_intcode(program))