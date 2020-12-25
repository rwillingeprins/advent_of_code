with open('input/day19.txt') as file:
    rules_string, messages_string = file.read().split('\n\n', 2)
rule_lookup = dict(line.split(': ', 2) for line in rules_string.splitlines())
messages = messages_string.splitlines()


def is_valid_message(message, rule_queue):
    if not message or not rule_queue:
        return bool(not message and not rule_queue)
    rule_id = rule_queue.pop(0)
    rule = rule_lookup[rule_id]
    if rule[0] == '"':
        if message[0] == rule[1]:
            return is_valid_message(message[1:], rule_queue)
        return False
    return any(is_valid_message(message, rule_option.split(' ') + rule_queue) for rule_option in rule.split(' | '))


def day19a():
    return sum(is_valid_message(message, ['0']) for message in messages)


def day19b():
    rule_lookup['8'] = '42 | 42 8'
    rule_lookup['11'] = '42 31 | 42 11 31'
    return sum(is_valid_message(message, ['0']) for message in messages)


print(day19a())
print(day19b())
