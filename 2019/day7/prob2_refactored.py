import sys
sys.path.append('../lib')

from itertools import permutations

from intcode import Intcode

def calc_thrust(phase_sequence, instructions):
    halts = 0
    next_input = 0
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

program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase_sequence = [9,8,7,6,5]
thrust = calc_thrust(phase_sequence, program)
print(thrust)
sys.exit(1)

with open('in.txt') as fh:
    program = [ int(i) for i in fh.read().strip().split(',') ]

max_thrust = 0
for comb in permutations([5, 6, 7, 8, 9]):
    comb_ints = [ int(digit) for digit in comb ]
    thrust = int(calc_thrust(comb_ints, program))
    max_thrust = max(thrust, max_thrust)

print(max_thrust)
