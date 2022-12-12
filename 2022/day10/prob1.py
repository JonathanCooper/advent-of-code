

class Instruction(object):

    def __init__(self, v):
        self.value = v
        self.cycles_left = 1

    def __repr__(self):
        return f'Instruction({self.value})'

class Circuit(object):

    def __init__(self, instructions):
        self.x = 1
        self.instr_list = instructions
        self.cycles_ran = 0
        self.running = None
        self.total_sig_strength = 0
        self.next_checkpoint = 20

    def run_cycle(self):
        #print(f'running cycle {self.cycles_ran + 1}')
        #print(f'instruction list: {self.instr_list}')
        #print(f'pending insrtuctions: {self.pending}')
        #print(f'x is {self.x}\n')
        this_cycle = self.cycles_ran + 1
        if this_cycle == self.next_checkpoint:
            self.next_checkpoint += 40
            #print(f'cycle {this_cycle}, x {self.x}, strength {this_cycle * self.x}')
            self.total_sig_strength += this_cycle * self.x
        if self.running:
            self.running.cycles_left -= 1
            if self.running.cycles_left == 0:
                self.x += self.running.value
                self.running = None
        elif len(self.instr_list) > 0:
            next_instr = self.instr_list.pop(0)
            if next_instr.startswith('addx'):
                v = int(next_instr.split()[-1])
                instr = Instruction(v)
                self.running = instr
        self.cycles_ran += 1
        #print(f'ran cycle {self.cycles_ran}')
        #print(f'instruction list: {self.instr_list}')
        #print(f'pending insrtuctions: {self.pending}')
        #print(f'x is {self.x}\n')


instructions = []
with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        instructions.append(line)

circuit = Circuit(instructions)

for _ in range(220):
    circuit.run_cycle()

print(circuit.total_sig_strength)

