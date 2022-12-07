from collections import namedtuple

File = namedtuple('File', 'size name')

class Dir(object):


    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = {}
        self.files = []

    def add_subdir(self, subdir):
        self.subdirs[subdir.name] = subdir

    def add_file(self, f):
        self.files.append(f)

    def get_size_direct(self):
        return sum([ f.size for f in self.files ])

    def get_size_recursive(self, max_size=None):
        global result
        total = 0
        for d in self.subdirs.values():
            d_size = d.get_size_recursive(max_size)
            total += d_size
        total += self.get_size_direct()
        if max_size and total <= max_size:
            #print(f'updating total for {self.name}, adding {total}')
            result += total
        return total

    def get_subdir(self, name):
        return self.subdirs[name]

    def get_all_sizes(self):
        candidates = []
        for d in self.subdirs.values():
            candidates += d.get_all_sizes()
        candidates.append(self.get_size_recursive())
        return candidates

        
current_dir = None

with open('in.txt') as fh:
    for line in fh:
        line = line.strip()
        if line.startswith('$'):
            if 'cd' in line:
                if line.endswith('..'):
                    current_dir = current_dir.parent
                else:
                    name = line.split()[-1]
                    try:
                        current_dir = current_dir.get_subdir(name)
                    except AttributeError:
                        current_dir = Dir('/')
        else:
            s = line.split()
            if s[0] == 'dir':
                new_sub = Dir(s[1], current_dir)
                current_dir.add_subdir(new_sub)
            else:
                new_file = File(int(s[0]), s[1])
                current_dir.add_file(new_file)

result = []
while current_dir.parent != None:
    current_dir = current_dir.parent


TOTAL = 70000000
NEEDED = 30000000

used = current_dir.get_size_recursive()
unused = TOTAL - used
to_delete = NEEDED - unused


#print(current_dir.get_all_sizes())
print(
    min(
        [ dirsize for dirsize in current_dir.get_all_sizes() if dirsize >= to_delete ]
    )
)
