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

def remove_units(input_str, lower):
    new_str = ''
    for char in input_str:
        if char != lower and ord(char) != ord(lower) - 32:
            new_str += char
    return new_str

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile) as fh:
        puzzle_input = fh.read()
        seen_units = set()
        shortest_length = len(puzzle_input)
        for char in puzzle_input:
            lower_char = char.lower()
            if lower_char in seen_units:
                continue
            seen_units.add(lower_char)
            trimmed_str = remove_units(puzzle_input, lower_char)
            puzzle_answer = remove_pairs(trimmed_str)
            #print(f'removing all {lower_char} units, length is {len(puzzle_answer)}')
            if len(puzzle_answer) < shortest_length:
                shortest_length = len(puzzle_answer)

    print(shortest_length)
