import sys

def find_freq():
    infile = sys.argv[1]
    current_freq = 0
    seen = set()
    while True:
        with open(infile) as fh:
            for line in fh:
                next = int(line.strip())
                current_freq += next
                if current_freq in seen:
                    return current_freq   
                else:
                    seen.add(current_freq) 

if __name__ == '__main__':
    res = find_freq()
    print(res)
