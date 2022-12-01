
def hex2bin(hex_str):
    d = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    return ''.join([ d[c] for c in hex_str ])


def bin2dec(b):
    return int(b, 2)

class Packet(object):


    def __init__(self, bin_str):
        self.bin_str = bin_str
        self.version = bin2dec(self.bin_str[:3])
        self.type = bin2dec(self.bin_str[3:6])
        self.blocksize = 5

    def read_blocks(self, s):
        start = 0
        done = False
        num_str = ''
        while not done:
            block = s[start:start + self.blocksize]
            prefix, group = block[0], block[1:]
            num_str += group
            start += self.blocksize
            if prefix == '0':
                done = True
        return bin2dec(num_str)

    def get_literal(self):
        if self.type != 4:
            raise ValueError(f'Packet is not a literal, type is {self.type}')
        return self.read_blocks(self.bin_str[6:])

    def subpackets(self):
        if self.type == 4:
            raise ValueError(f'Literal type packets contain no subpackets')
        length_type = self.bin_str[6]
        if length_type == '0':
            #print(f'L bits: {self.bin_str[7:22]}')
            sub_packet_len = bin2dec(self.bin_str[7:22])
            return self.split_packets(self.bin_str[22:sub_packet_len + 22])
            #print(f'length type: {length_type}, sub_packet_len: {sub_packet_len}, packet data: {self.bin_str[22:sub_packet_len + 22]}')

    def split_packets(self, packet_str):
        # dumb recrusive shit

packet = Packet(hex2bin('38006F45291200'))
packet.subpackets()
