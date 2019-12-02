
def required_fuel(mass):
    req = mass // 3 - 2
    if req <= 0:
        return 0
    else:
        return req + required_fuel(req)


with open('in1.txt') as fh:
    total = 0
    for line in fh:
        mass = int(line.strip())
        req = required_fuel(mass)
        total += req

print(total)
