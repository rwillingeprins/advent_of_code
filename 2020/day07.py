import re

contents_per_color = {}
with open('input/day07.txt') as file:
    for line in file:
        container_color, contained_bags_string = line.strip('\n.').split(' bags contain ')
        contained_bag_strings = contained_bags_string.split(', ')
        number_per_color = {}
        for contained_bag_string in contained_bag_strings:
            if contained_bag_string == 'no other bags':
                continue
            content_number, content_color = re.match(r'(\d+) (\w+ \w+) bags?$', contained_bag_string).groups()
            number_per_color[content_color] = int(content_number)
        contents_per_color[container_color] = number_per_color

recursive_contents_per_color = {}


def get_recursive_contents_for_color(container_color):
    if container_color in recursive_contents_per_color:
        return recursive_contents_per_color[container_color]
    else:
        number_per_color = contents_per_color[container_color]
        recursive_number_per_color = number_per_color.copy()
        for color, number in number_per_color.items():
            inner_recursive_number_per_color = get_recursive_contents_for_color(color)
            for inner_color, inner_number in inner_recursive_number_per_color.items():
                recursive_number_per_color.setdefault(inner_color, 0)
                recursive_number_per_color[inner_color] += number * inner_number
        return recursive_number_per_color


def day07a():
    return sum('shiny gold' in get_recursive_contents_for_color(color) for color in contents_per_color)


def day07b():
    recursive_number_per_color = get_recursive_contents_for_color('shiny gold')
    return sum(n for n in recursive_number_per_color.values())


print(day07a())
print(day07b())
