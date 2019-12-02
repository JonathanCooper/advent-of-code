

def required_fuel(mass):
    return mass // 3 - 2


with open('in1.txt') as fh:
    total = 0
    for line in fh:
        mass = int(line.strip())
        req = required_fuel(mass)
        total += req

print(total)
