def transform(value, subject_number):
    return (value * subject_number) % 20201227


public_keys = [9717666, 20089533]
key = 1
loop_size = 0
while key != public_keys[0]:
    key = transform(key, 7)
    loop_size += 1

key = 1
for _ in range(loop_size):
    key = transform(key, public_keys[1])

print(key)
