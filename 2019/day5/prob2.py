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


    def __init__(self, instructions, program_input):
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
        self.input = program_input
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
        self.instructions[val] = str(self.input)
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

#testcases = [
#    "3,9,8,9,10,9,4,9,99,-1,8",
#    "3,9,7,9,10,9,4,9,99,-1,8",
#    "3,3,1108,-1,8,3,4,3,99",
#    "3,3,1107,-1,8,3,4,3,99",
#]
#
program = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
#program = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
#for test_val in [0, 4, 8, 9, 1000]:
#for test_val in [1000]:
#    instructions = program.split(',')
#    computer = Intcode(instructions, test_val)
#    output = computer.run()
#    print(f'{test_val}, {output}')
#sys.exit(1)
#
#instructions = testcase.split(',')
#computer = Intcode(instructions, 5)
#output = computer.run()
#print(output)
#sys.exit(1)
#for testcase in testcases:
#    instructions = testcase.split(',')
#    computer = Intcode(instructions, 5)
#    output = computer.run()
#    print(f'{testcase}: {output}')
#
#sys.exit(1)

with open('in.txt') as fh:
    raw = fh.read()
    instructions = [ word for word in raw.split(',') ]
    computer = Intcode(instructions, 5)
    output = computer.run()
    print(output)

