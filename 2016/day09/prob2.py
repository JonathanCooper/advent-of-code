
def compressed_len(seq):
    #print(f"compressed_len() called with {seq}")
    if len(seq) == 0:
        return 0
    non_marker_prefix_len = 0
    if seq.startswith("("):
        seq = seq[1:]
        end_of_marker = seq.index(")")
        marker_content = seq[:end_of_marker]
        repeat_chars, repeat_num = [ int(num) for num in marker_content.split("x") ]
        total_len = 0
        for _ in range(repeat_num):
            total_len += compressed_len(seq[end_of_marker + 1:end_of_marker + repeat_chars + 1])
        return total_len + compressed_len(seq[end_of_marker + repeat_chars + 1:])
    # else:
    for i, c in enumerate(seq):
        if c != "(":
            non_marker_prefix_len += 1
        else:
            return non_marker_prefix_len + compressed_len(seq[i:])
    return non_marker_prefix_len

"""
    while len(seq) > 0:
        c = seq[0]
        seq = seq[1:] # seq = 1x5)BC
        if c != '(':
            new_str += c
        else:
            end_of_marker = seq.index(")") # 3
            marker_content = seq[:end_of_marker] # 1x5
            repeat_chars, repeat_num = [ int(num) for num in marker_content.split("x") ]
            for _ in range(repeat_num):
                #print(f"loop {_}: adding {seq[end_of_marker + 1:end_of_marker + repeat_chars + 1]}")
                #print(f"debug end_of_marker: {end_of_marker}, repeat_chars: {repeat_chars}")
                new_str += seq[end_of_marker + 1:end_of_marker + repeat_chars + 1] # seq[4:5]
            seq = seq[end_of_marker + repeat_chars + 1:] # seq[5:]
    #print(new_str)
    return new_str
"""

def run_tests():
    assert(compressed_len("(3x3)XYZ") == len("XYZXYZXYZ"))
    assert(compressed_len("X(8x2)(3x3)ABCY") == len("XABCABCABCABCABCABCY"))
    assert(compressed_len("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920)
    assert(compressed_len("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445)

run_tests()

with open("in.txt") as fh:
    line = fh.readline()
    line = line.strip()
    print(compressed_len(line))
