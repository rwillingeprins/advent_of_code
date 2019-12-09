width, height = 25, 6
n_layer_pixels = width * height
with open('day08.txt') as input_file:
    input_string = input_file.readline()
pixel_values = list(map(int, list(input_string)))
layers = [pixel_values[i:i + n_layer_pixels] for i in range(0, len(pixel_values), n_layer_pixels)]
min_zero_count = n_layer_pixels
target_layer = layers[0]
layer_index = 0
for layer in layers:
    zero_count = 0
    for pixel_value in layer:
        if pixel_value == 0:
            zero_count += 1
    if zero_count < min_zero_count:
        min_zero_count = zero_count
        target_layer = layer
print(min_zero_count)
one_count = 0
two_count = 0
for pixel_value in target_layer:
    if pixel_value == 1:
        one_count += 1
    elif pixel_value == 2:
        two_count += 1
print(one_count * two_count)
