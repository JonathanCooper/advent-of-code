import sys
from operator import itemgetter

class Guard():

    def __init__(self):
        self.total_sleeping = 0
        self.minute_counts = {}

    def bump_minute(self, n):
        try:
            self.minute_counts[n] += 1
        except KeyError:
            self.minute_counts[n] = 1
        
        self.total_sleeping += 1

    def most_freq_min(self):
        s = sorted(self.minute_counts.items(), key=lambda x: x[1], reverse=True)
        return s[0][0]

def get_minute(line):
    return int(line.split()[1].rstrip(']').split(':')[1])

def line_to_tup(line):
    split = line.split()
    date = split[0].lstrip('[')
    month, day = date.split('-')[1:]
    time = split[1].rstrip(']')
    hour, minute = time.split(':')
    msg = ' '.join(split[2:])
    return (int(month), int(day), int(hour), int(minute), msg)

def linesort(lines):
    return sorted(lines, key=itemgetter(0, 1, 2, 3))

if __name__ == '__main__':
    infile = sys.argv[1]
    guard_info = {}
    lines = []
    with open(infile) as fh:
        for line in fh:
            line = line.strip()
            line = line_to_tup(line)
            lines.append(line)
    sorted_log = linesort(lines)
    for line in sorted_log:
        msg = line[4]
        if msg.endswith('begins shift'):
            guard_id = int(msg.split()[1].lstrip('#'))
            try:
                on_duty_guard = guard_info[guard_id]
            except KeyError:
                on_duty_guard = Guard()
                guard_info[guard_id] = on_duty_guard
        if msg.endswith('falls asleep'):
            start = line[3]
        if msg.endswith('wakes up'):
            end = line[3]
            for i in range(start, end):
                on_duty_guard.bump_minute(i)
    
    most_mins = 0
    for k, v in guard_info.items():
        if v.total_sleeping > most_mins:
            #print(k, v.total_sleeping, most_mins)
            most_mins = v.total_sleeping
            most_guard = int(k)
    print(f'sleepiest guard was {most_guard}')
    sleepiest_min = guard_info[most_guard].most_freq_min()
    print(f'sleepiest minute was {sleepiest_min}')
    print(f'puzzle answer most_guard * sleepiest_min: {most_guard * sleepiest_min}')
