import sys
from itertools import permutations

def instruction_split(instruction):
    opcode = instruction[-2:].lstrip('0')
    params = instruction[:-2]
    return (params, opcode)

class Operation(object):

    def __init__(self, function, num_params):
        self.function = function
        self.num_params = num_params


class Intcode(object):


    def __init__(self, instructions, program_inputs):
        self.instructions = list(instructions)
        self.cursor = 0
        self.operations = {
            '1': Operation(self.add, 3),
            '2': Operation(self.multiply, 3),
            '3': Operation(self.get_input, 1),
            '4': Operation(self.store_output, 1),
            '5': Operation(self.jump_true, 2),
            '6': Operation(self.jump_false, 2),
            '7': Operation(self.less_than, 3),
            '8': Operation(self.equals, 3),
            '99': Operation(self.halt, 0),
        }
        self.inputs = program_inputs
        self.output = None
        self.halted = False

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
        old_cursor = self.cursor
        modified = operation.function(param_list)
        # operation functions return True if they have modified the instruction pointer, False if not
        # if modified == False, we increment the instruction pointer
        if not modified:
            self.cursor += operation.num_params + 1
        #print(f'Ran {opcode}; res: {self.instructions}, old cur: {old_cursor} new cur: {self.cursor}')
        return opcode

    def add(self, param_list):
        val1, val2, target = param_list
        #print(f'ADD: setting position {target} to {int(self.instructions[val1]) + int(self.instructions[val2])}')
        self.instructions[target] = str(int(self.instructions[val1]) + int(self.instructions[val2]))
        return False

    def multiply(self, param_list):
        val1, val2, target = param_list
        #print(f'MULT: setting position {target} to {int(self.instructions[val1]) * int(self.instructions[val2])}')
        self.instructions[target] = str(int(self.instructions[val1]) * int(self.instructions[val2]))
        return False

    def jump_true(self, param_list):
        test_val_address, goto_address = [ int(param) for param in param_list ]
        if self.instructions[test_val_address] != '0':
            self.cursor = int(self.instructions[goto_address])
            return True
        else:
            return False

    def jump_false(self, param_list):
        test_val_address, goto_address = [ int(param) for param in param_list ]
        if self.instructions[test_val_address] == '0':
            #print(f'DEBUG: setting instruction pointer to value at address {test_val_address} ({self.instructions[goto_address]}')
            self.cursor = int(self.instructions[goto_address])
            return True
        else:
            return False

    def less_than(self, param_list):
        cmp_val_address1, cmp_val_address2, dest_address = [ int(param) for param in param_list ]
        if int(self.instructions[cmp_val_address1]) < int(self.instructions[cmp_val_address2]):
            self.instructions[dest_address] = '1'
        else:
            self.instructions[dest_address] = '0'
        return False

    def equals(self, param_list):
        cmp_val_address1, cmp_val_address2, dest_address = [ int(param) for param in param_list ]
        if int(self.instructions[cmp_val_address1]) == int(self.instructions[cmp_val_address2]):
            self.instructions[dest_address] = '1'
        else:
            self.instructions[dest_address] = '0'
        return False

    def get_input(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        #print(f'IN: setting position {val} to {self.input}')
        self.instructions[val] = str(self.inputs[0])
        del self.inputs[0]
        return False

    def store_output(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        #print(f'OUT: setting output to {self.instructions[val]}')
        self.output = str(self.instructions[val])
        return False

    def halt(self, param_list):
        if len(param_list) > 0:
            raise Exception(f'Wrong number of params to halt: {param_list}')
        return False

    def run(self):
        last_op = None
        while last_op not in ['99', '4']:
            last_op = self.process_op()
        return last_op == '99'

    def __repr__(self):
        return f'Intcode({self.instructions})'

def calc_thrust(phase_sequence, instructions):
    halts = 0
    next_input = '0'
    amps = {}
    for phase in phase_sequence:
        amps[phase] = Intcode(instructions, [phase])
    while halts < 5:
        for phase in phase_sequence:
            computer = amps[phase]
            computer.inputs.append(next_input)
            halted = computer.run()
            if halted:
                halts += 1
            next_input = computer.output
    return next_input

with open('in.txt') as fh:
    program = fh.read().strip().split(',')

#phase_sequence = [9,8,7,6,5]
#thrust = calc_thrust(phase_sequence, program)
#print(thrust)
#sys.exit(1)

max_thrust = 0
for comb in permutations([5, 6, 7, 8, 9]):
    comb_ints = [ int(digit) for digit in comb ]
    thrust = int(calc_thrust(comb_ints, program))
    max_thrust = max(thrust, max_thrust)

print(max_thrust)
