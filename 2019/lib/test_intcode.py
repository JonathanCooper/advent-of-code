from intcode import Intcode

test_program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phase_sequence = [4,3,2,1,0]

def calc_thrust(phase_sequence, instructions):
    next_input = 0
    amps = {}
    for phase in phase_sequence:
        computer = Intcode(instructions, [phase, next_input])
        halted = computer.run()
        next_input = computer.output
    return next_input

assert(calc_thrust(phase_sequence, test_program) == 43210)

print('OK')
