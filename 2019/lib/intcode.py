class Operation(object):

    def __init__(self, function, num_params):
        self.function = function
        self.num_params = num_params


class Intcode(object):


    def __init__(self, instructions, program_inputs):
        self.instructions = list(instructions)
        self.cursor = 0
        self.operations = {
            1: Operation(self.add, 3),
            2: Operation(self.multiply, 3),
            3: Operation(self.get_input, 1),
            4: Operation(self.store_output, 1),
            5: Operation(self.jump_true, 2),
            6: Operation(self.jump_false, 2),
            7: Operation(self.less_than, 3),
            8: Operation(self.equals, 3),
            99: Operation(self.halt, 0),
        }
        self.inputs = program_inputs
        self.output = None

    def instruction_split(self, instruction):
        instruction = str(instruction)
        opcode = int(instruction[-2:])
        params = [ int(i) for i in instruction[:-2] ]
        return (params, opcode)

    def process_op(self):
        instruction = self.instructions[self.cursor]
        param_modes, opcode = self.instruction_split(instruction)
        operation = self.operations[opcode]
        param_list = []
        for i in range(1, operation.num_params + 1):
            try:
                param_mode = param_modes[-i]
            except IndexError:
                param_mode = 0
            if param_mode == 1:
                val = self.cursor + i
            elif param_mode == 0:
                val = self.instructions[self.cursor + i]
            else:
                raise Exception(f'Unknown parameter mode: {param_mode} ({type(param_mode)})')
            param_list.append(val)
        old_cursor = self.cursor
        modified = operation.function(param_list)
        if not modified:
            self.cursor += operation.num_params + 1
        return opcode

    def add(self, param_list):
        val1, val2, target = param_list
        self.instructions[target] = self.instructions[val1] + self.instructions[val2]
        return False

    def multiply(self, param_list):
        val1, val2, target = param_list
        self.instructions[target] = self.instructions[val1] * self.instructions[val2]
        return False

    def jump_true(self, param_list):
        test_val_address, goto_address = param_list
        if self.instructions[test_val_address] != 0:
            self.cursor = self.instructions[goto_address]
            return True
        else:
            return False

    def jump_false(self, param_list):
        test_val_address, goto_address = param_list
        if self.instructions[test_val_address] == 0:
            self.cursor = self.instructions[goto_address]
            return True
        else:
            return False

    def less_than(self, param_list):
        cmp_val_address1, cmp_val_address2, dest_address = param_list
        if self.instructions[cmp_val_address1] < self.instructions[cmp_val_address2]:
            self.instructions[dest_address] = 1
        else:
            self.instructions[dest_address] = 0
        return False

    def equals(self, param_list):
        cmp_val_address1, cmp_val_address2, dest_address = param_list
        if self.instructions[cmp_val_address1] == self.instructions[cmp_val_address2]:
            self.instructions[dest_address] = 1
        else:
            self.instructions[dest_address] = 0
        return False

    def get_input(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        self.instructions[val] = self.inputs[0]
        del self.inputs[0]
        return False

    def store_output(self, param_list):
        if len(param_list) != 1:
            raise Exception(f'Wrong number of params to get_input: {param_list}')
        val = param_list[0]
        self.output = self.instructions[val]
        return False

    def halt(self, param_list):
        if len(param_list) > 0:
            raise Exception(f'Wrong number of params to halt: {param_list}')
        return False

    def run(self):
        last_op = None
        while last_op not in [99, 4]:
            last_op = self.process_op()
        return last_op == 99

    def __repr__(self):
        return f'Intcode({self.instructions})'

    def __str__(self):
        return str(self.instructions[0])
