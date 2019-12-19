class IntcodeComputer(object):
    def __init__(self, program, inputs):

        self.intcode = program
        self.in_data = inputs

        self.out_data = []

        self.i_program = 0

    def get_val(self, r, p_imm):
        return (r if p_imm else self.intcode[r])

    def op01_add(self, p_imm):
        [r0, r1, i_w] = self.intcode[(self.i_program+1) : (self.i_program+4)]
        
        self.intcode[i_w] = self.get_val(r0, p_imm[0]) + self.get_val(r1, p_imm[1])

        self.i_program += 4

    def op02_mul(self, p_imm):
        [r0, r1, i_w] = self.intcode[(self.i_program+1) : (self.i_program+4)]
        
        self.intcode[i_w] = self.get_val(r0, p_imm[0]) * self.get_val(r1, p_imm[1])

        self.i_program += 4

    def op03_inp(self, p_imm):
        i_w = self.intcode[self.i_program + 1]

        self.intcode[i_w] = self.in_data

        self.i_program += 2

    def op04_oup(self, p_imm):
        r0 = self.intcode[self.i_program + 1]

        self.out_data = self.get_val(r0, p_imm[0])

        self.i_program += 2

    def op05_jit(self, p_imm):
        [r0, r1] = self.intcode[(self.i_program+1) : (self.i_program+3)]

        if self.get_val(r0, p_imm[0]) != 0:
            self.i_program = self.get_val(r1, p_imm[1])
        
        else:
            self.i_program += 3

    def op06_jif(self, p_imm):
        [r0, r1] = self.intcode[(self.i_program+1) : (self.i_program+3)]

        if self.get_val(r0, p_imm[0]) == 0:
            self.i_program = self.get_val(r1, p_imm[1])
        
        else:
            self.i_program += 3

    def op07_les(self, p_imm):
        [r0, r1, i_w] = self.intcode[(self.i_program+1) : (self.i_program+4)]

        self.intcode[i_w] = self.get_val(r0, p_imm[0]) < self.get_val(r1, p_imm[1])

        self.i_program += 4
    
    def op08_eql(self, p_imm):
        [r0, r1, i_w] = self.intcode[(self.i_program+1) : (self.i_program+4)]

        self.intcode[i_w] = self.get_val(r0, p_imm[0]) == self.get_val(r1, p_imm[1])

        self.i_program += 4

    def op99_end(self, p_imm):
        pass

    def execute_step(self):
        (p_mode_int, op_code) = divmod(self.intcode[self.i_program], 100)

        p_immediate = (p_mode_int % 10, (p_mode_int % 100) >= 10, p_mode_int >= 1000)

        if op_code == 1:
            self.op01_add(p_immediate)
        
        elif op_code == 2:
            self.op02_mul(p_immediate)

        elif op_code == 3:
            self.op03_inp(p_immediate)

        elif op_code == 4:
            self.op04_oup(p_immediate)

        elif op_code == 5:
            self.op05_jit(p_immediate)

        elif op_code == 6:
            self.op06_jif(p_immediate)

        elif op_code == 7:
            self.op07_les(p_immediate)

        elif op_code == 8:
            self.op08_eql(p_immediate)

        elif op_code == 99:
            self.op99_end(p_immediate)
            return False

        else:
            print('Invalid OP code...')

        return True

    def run_till_end(self):
        while self.execute_step():
            continue

        return self.out_data



input_file = open('D05/.input', 'r')

input_text = input_file.read()

input_file.close()

program = [int(s) for s in input_text.split(',')]

int_comp = IntcodeComputer(program, 5)

print("Output code:", int_comp.run_till_end())