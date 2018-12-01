import sys

if __name__ == '__main__':
    infile = sys.argv[1]
    current_freq = 0
    with open(infile) as fh:
        for line in fh:
            next = int(line.strip())
            current_freq += next
    print(current_freq)
