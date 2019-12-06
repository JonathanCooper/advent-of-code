import sys

def instruction_split(instruction):
    opcode = instruction[-2:].lstrip('0')
    params = instruction[:-2]
    return (params, opcode)

class Operation(object):

    def __init__(self, function, num_params):
        self.function = function
        self.num_params = num_params


class Intcode(object):


    def __init__(self, instructions):
        self.instructions = list(instructions)
        self.cursor = 0
        self.operations = {
            '1': Operation(self.add, 3),
            '2': Operation(self.multiply, 3),
            '3': Operation(self.get_input, 1),
            '4': Operation(self.store_output, 1),
            '99': Operation(self.halt, 0),
        }
        self.input = 1
        self.output = None

    def process_op(self):
        #print(self.instructions[self.cursor:self.cursor + 4])
        instruction = self.instructions[self.cursor]
        param_modes, opcode = instruction_split(instruction)
        operation = self.operations[opcode]
        param_list = []
        for i in range(1, operation.num_params + 1):
            try:
                param_mode = param_modes[-i]
            except IndexError:
                param_mode = '0'

            if param_mode == '1':
                val = self.cursor + i
            elif param_mode in set(['0', '']):
                val = self.instructions[self.cursor + i]
                #print(f'pointer: {pointer}, val: {val}')
            else:
                raise Exception(f'Unknown parameter mode: {param_mode} ({type(param_mode)})')
            param_list.append(int(val))
            #print(f'adding param: {val}, opcode: {opcode}, i: {i}, param_list: {param_list}, param_mode: {param_mode}, self.cursor: {self.cursor}')
        #print(f'opcode: {opcode}, num_params: {operation.num_params}')
        operation.function(param_list)
        self.cursor += operation.num_params + 1
        return opcode

    def add(self, param_list):
        val1, val2, target = param_list
        #print(f'ADD: setting position {target} to {int(self.instructions[val1]) + int(self.instructions[val2])}')
        self.instructions[target] = str(int(self.instructions[val1]) + int(self.instructions[val2]))

    def multiply(self, param_list):
        val1, val2, target = param_list
        #print(f'MULT: setting position {target} to {int(self.instructions[val1]) * int(self.instructions[val2])}')
        self.instructions[target] = str(int(self.instructions[val1]) * int(self.instructions[val2]))

    def get_input(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        #print(f'IN: setting position {val} to {self.input}')
        self.instructions[val] = str(self.input)

    def store_output(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        #print(f'OUT: setting output to {self.instructions[val]}')
        self.output = str(self.instructions[val])

    def halt(self, param_list):
        if len(param_list) > 0:
            raise Exception(f'Wrong number of params to halt: {param_list}')
        return self.output

    def run(self):
        last_op = None
        while last_op != '99':
            last_op = self.process_op()
            #print(repr(self))
            #print('*****')
        return self.output    
    def __repr__(self):
        return f'Intcode({self.instructions})'

    def __str__(self):
        return str(self.instructions[0])

#computer = Intcode('1002,4,3,4,33'.split(','))
#computer.run()
#sys.exit(1)

with open('in.txt') as fh:
    raw = fh.read()
    instructions = [ word for word in raw.split(',') ]
    computer = Intcode(instructions)
    output = computer.run()
    print(output)

