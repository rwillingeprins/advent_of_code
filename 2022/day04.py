assignment_pairs = [
    tuple(int(section) for assignment in line.strip().split(',') for section in assignment.split('-'))
    for line in open('input/day04.txt')
]
print(sum(int(s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1) for s1, e1, s2, e2 in assignment_pairs))
print(sum(int(s1 <= s2 <= e1 or s2 <= s1 <= e2) for s1, e1, s2, e2 in assignment_pairs))
