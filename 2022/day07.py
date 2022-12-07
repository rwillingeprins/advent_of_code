with open('input/day07.txt') as input_file:
    _, *io_strings = input_file.read().split('$ ')
current_directory = root = {'size': 0}
directories = [root]
for io_string in io_strings:
    if io_string.startswith('cd'):
        _, dir_name = io_string.strip().split()
        if dir_name == '/':
            current_directory = root
        elif dir_name == '..':
            current_directory = current_directory['parent']
        else:
            current_directory = {'parent': current_directory, 'size': 0}
            directories.append(current_directory)
    elif io_string.startswith('ls'):
        size = sum(int(entry.split()[0]) for entry in io_string.splitlines()[1:] if not entry.startswith('dir'))
        parent_directory = current_directory
        while parent_directory:
            parent_directory['size'] += size
            parent_directory = parent_directory.get('parent')
sizes = [directory['size'] for directory in directories]
print(sum(size for size in sizes if size <= 100000))
required_space = root['size'] - 40000000
print(next(size for size in sorted(sizes) if size >= required_space))
