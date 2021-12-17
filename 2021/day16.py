from functools import reduce


class Bits:
    def __init__(self, hexadecimal):
        self.bits = bin(int('1' + hexadecimal, 16))[3:]
        self.index = 0

    def read_binary(self, n=1):
        bits = self.bits[self.index: self.index + n]
        self.index += n
        return bits

    def read_int(self, n=1):
        return int(self.read_binary(n), 2)


class Packet:
    def __init__(self, bits):
        self.version = bits.read_int(3)
        self.type_id = bits.read_int(3)
        if self.type_id == 4:
            keep_reading = bits.read_int()
            binary_literal = bits.read_binary(4)
            while keep_reading:
                keep_reading = bits.read_int()
                binary_literal += bits.read_binary(4)
            self.literal_value = int(binary_literal, 2)
        else:
            self.sub_packets = []
            length_type_id = bits.read_int()
            if length_type_id:
                n_sub_packets = bits.read_int(11)
                while len(self.sub_packets) < n_sub_packets:
                    self.sub_packets.append(Packet(bits))
            else:
                n_bits = bits.read_int(15)
                start_index = bits.index
                while bits.index < start_index + n_bits:
                    self.sub_packets.append(Packet(bits))

    @property
    def version_sum(self):
        version_sum = self.version
        if self.type_id != 4:
            for sub_packet in self.sub_packets:
                version_sum += sub_packet.version_sum
        return version_sum

    @property
    def value(self):
        if self.type_id == 0:
            return sum(sub_packet.value for sub_packet in self.sub_packets)
        if self.type_id == 1:
            return reduce(lambda x, y: x * y, (sub_packet.value for sub_packet in self.sub_packets))
        if self.type_id == 2:
            return min(sub_packet.value for sub_packet in self.sub_packets)
        if self.type_id == 3:
            return max(sub_packet.value for sub_packet in self.sub_packets)
        if self.type_id == 4:
            return self.literal_value
        if self.type_id == 5:
            return int(self.sub_packets[0].value > self.sub_packets[1].value)
        if self.type_id == 6:
            return int(self.sub_packets[0].value < self.sub_packets[1].value)
        if self.type_id == 7:
            return int(self.sub_packets[0].value == self.sub_packets[1].value)


with open('input/day16.txt') as file:
    packet = Packet(Bits(file.read().strip()))
print(packet.version_sum)
print(packet.value)
