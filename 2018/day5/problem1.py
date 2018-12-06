import sys

def reactive_pair(chrA, chrB):
    #print(f'comparing {chrA}, {chrB}: {abs(ord(chrA) - ord(chrB)) == 32}')
    return abs(ord(chrA) - ord(chrB)) == 32

def remove_pairs(input_str):
    new_str = ''
    i = 0
    while i < len(input_str) - 1:
        this_char, next_char = input_str[i], input_str[i + 1]
        if reactive_pair(this_char, next_char):
            i += 2
            while True:
                try:
                    this_char, next_char = new_str[-1], input_str[i]
                except IndexError:
                    break
                if reactive_pair(this_char, next_char):
                    new_str = new_str[:-1]
                    i += 1
                else:
                    break
                    #i += 1
                    #continue
        else: 
            new_str += this_char
            i += 1
    return new_str

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile) as fh:
        puzzle_input = fh.read()
        puzzle_answer = remove_pairs(puzzle_input)
        print(len(puzzle_answer))
