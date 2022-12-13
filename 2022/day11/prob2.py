
class Monkey(object):

    def __init__(self):
        self.items = []
        self.inspected = 0
    
    def add_item(self, item):
        self.items.append(int(item))

    def set_operation(self, operator, value):
        self.operator = operator
        self.op_value = value

    def set_test(self, value, true_monkey, false_monkey):
        self.test_value = int(value)
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def inspect_all_items(self):
        for item in self.items:
            #print(f'inspecting item {item}')
            worry_level = self.run_operation(item)
            #print(f'worry level is {worry_level}')
            self.inspected += 1
            if self.run_test(worry_level):
                self.true_monkey.add_item(worry_level)
            else:
                self.false_monkey.add_item(worry_level)
        #print('turn complete')    
        self.items = []

    def run_operation(self, item):
        if self.op_value:
            op_value = self.op_value
        else:
            op_value = item
        if self.operator == '*':
            return item * op_value
        elif self.operator == '+':
            return item + op_value
        else:
            raise ValueError(f'Unexpected operator: {self.operator}')

    def run_test(self, item):
        return item % self.test_value == 0

    def __repr__(self):
        return str(self.items)

def run_round(n=1):
    for _ in range(n):
        for i in sorted(monkeys.keys()):
            monkey = monkeys[i]
            print(f'round {_} monkey {i} items: {len(monkey.items)}')
            monkey.inspect_all_items()

monkeys = {}
for i in range(8):
    monkeys[i] = Monkey()

with open('test.txt') as fh:
    for line in fh:
        line = line.strip()
        if line == '':
            continue
        split = line.split()
        if split[0] == 'Monkey':
            current_monkey_idx = int(split[1].rstrip(':'))
            current_monkey = monkeys[current_monkey_idx]
        elif split[0] == 'Starting':
            for item in split[2:]:
                item = item.rstrip(',')
                current_monkey.add_item(item)
        elif split[0] == 'Operation:':
            if split[5] == 'old':
                current_monkey.set_operation(split[4], None)
            else:
                current_monkey.set_operation(split[4], int(split[5]))
        elif split[0] == 'Test:':
            test_value = split[3]
        elif split[0] == 'If':
            if split[1] == 'true:':
                true_monkey_idx = int(split[5])
            elif split[1] == 'false:':
                false_monkey_idx = int(split[5])
                current_monkey.set_test(
                    test_value,
                    monkeys[true_monkey_idx],
                    monkeys[false_monkey_idx]
                )
            else:
                raise ValueError(f'Unexpected line: {line}')
        else:
            raise ValueError(f'Unexpected line: {line}')

for i in range(current_monkey_idx + 1, 8):
    del monkeys[i]

run_round(n=10000)
s = sorted(monkeys.values(), key=lambda x: x.inspected, reverse=True)
print(s[0].inspected * s[1].inspected)
