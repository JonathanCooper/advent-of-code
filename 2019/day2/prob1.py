import sys

class Intcode(object):

    def __init__(self, instructions):
        self.instructions = list(instructions)
        self.cursor = 0

    def initialize(self):
        self.instructions[1] = 12
        self.instructions[2] = 2

    def process_op(self):
        #print(self.instructions[self.cursor:self.cursor + 4])
        opcode = self.instructions[self.cursor]
        if opcode == 99:
            return opcode
        elif opcode == 1:
            self.add(self.instructions[self.cursor + 1:self.cursor + 4])
        elif opcode == 2:
            self.multiply(self.instructions[self.cursor + 1:self.cursor + 4])
        else:
            raise Exception(f'unknown opcode: {opcode}')
        self.cursor += 4
        return opcode

    def add(self, args):
        op1, op2, target = args
        #print(f'position {target} becomes {self.instructions[op1] + self.instructions[op2]}')
        self.instructions[target] = self.instructions[op1] + self.instructions[op2]

    def multiply(self, args):
        op1, op2, target = args
        self.instructions[target] = self.instructions[op1] * self.instructions[op2]

    def run(self):
        self.initialize()
        last_op = None
        while last_op != 99:
            last_op = self.process_op()
            #print(repr(self))
            #print('*****')
    
    def __repr__(self):
        return f'Intcode({self.instructions})'

    def __str__(self):
        return str(self.instructions[0])


with open('in.txt') as fh:
    raw = fh.read()
    instructions = [ int(i) for i in raw.split(',') ]
    computer = Intcode(instructions)
    computer.run()
    print(computer)
