datastream = open('input/day06.txt').read().strip()
packet_start = 4
while len(set(datastream[packet_start - 4:packet_start])) < 4:
    packet_start += 1
message_start = packet_start + 10
while len(set(datastream[message_start - 14:message_start])) < 14:
    message_start += 1
print(packet_start, message_start)
