width, height = 25, 6
n_layer_pixels = width * height
with open('day08.txt') as input_file:
    input_string = input_file.readline()
pixel_values = list(map(int, list(input_string)))
layers = [pixel_values[i:i + n_layer_pixels] for i in range(0, len(pixel_values), n_layer_pixels)]
image = [2] * n_layer_pixels
for layer in layers:
    for index, pixel_value in enumerate(layer):
        if image[index] == 2:
            image[index] = pixel_value

image_string = ''
for pixel_index, pixel_value in enumerate(image):
    if pixel_index % 25 == 0:
        image_string += '\n'
    if pixel_value == 0:
        image_string += ' '
    elif pixel_value == 1:
        image_string += '#'
print(image_string)
