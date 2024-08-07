
def compress(seq):
    """
    A(1x5)BC -> ABBBBBC
    """
    new_str = ''
    in_marker = False
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

def run_tests():
    assert(compress("ADVENT") == "ADVENT")
    assert(compress("A(1x5)BC") == "ABBBBBC")
    assert(compress("(3x3)XYZ") == "XYZXYZXYZ")
    assert(compress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG")
    assert(compress("(6x1)(1x3)A") == "(1x3)A")
    assert(compress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY")

run_tests()

with open("in.txt") as fh:
    line = fh.readline()
    line = line.strip()
    print(len(compress(line)))
