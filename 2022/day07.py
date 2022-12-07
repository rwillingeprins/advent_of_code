def get_size(entry):
    if 'size' in entry:
        return entry['size']
    return sum(get_size(child) for child in entry['children'].values())


with open('input/day07.txt') as input_file:
    _, *io_strings = input_file.read().split('$ ')
current_directory = root = {'children': {}}
directories = [root]
for io_string in io_strings:
    command_string, *output_lines = io_string.splitlines()
    command, *args = command_string.split()
    if command == 'cd':
        dir_name = args[0]
        if dir_name == '/':
            current_directory = root
        elif dir_name == '..':
            current_directory = current_directory['parent']
        else:
            current_directory = current_directory['children'][dir_name]
    elif command == 'ls':
        for list_item in output_lines:
            item_spec, name = list_item.split()
            entry = {'parent': current_directory}
            if item_spec == 'dir':
                entry['children'] = {}
                directories.append(entry)
            else:
                entry['size'] = int(item_spec)
            current_directory['children'][name] = entry
sizes = [get_size(directory) for directory in directories]
print(sum(size for size in sizes if size <= 100000))
required_space = get_size(root) - 40000000
print(next(size for size in sorted(sizes) if size >= required_space))
