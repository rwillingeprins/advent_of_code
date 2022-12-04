calorie_sums = [sum(map(int, elf.splitlines())) for elf in open('input/day01.txt').read().split('\n\n')]
print(max(calorie_sums))
print(sum(sorted(calorie_sums)[-3:]))
