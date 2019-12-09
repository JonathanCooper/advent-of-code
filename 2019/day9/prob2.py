import sys
sys.path.append('../lib')

from itertools import permutations

from intcode import Intcode

#program = [3,1985,109,19,204,-34]
#program = [1102,34915192,34915192,7,4,7,99,0]
#program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

with open('in.txt') as fh:
    program = [ int(i) for i in fh.read().strip().split(',') ]

computer = Intcode(program, [2])
computer.run()
#print(computer.instructions)
print(computer.stdout)
