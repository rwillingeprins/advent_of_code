def simulate_lanternfish(n_days):
    timer_counts = [0] * 9
    with open('input/day06.txt') as file:
        for timer in map(int, file.readline().split(',')):
            timer_counts[timer] += 1
    for _ in range(n_days):
        zero_count = timer_counts[0]
        for timer in range(8):
            timer_counts[timer] = timer_counts[timer + 1]
        timer_counts[6] += zero_count
        timer_counts[8] = zero_count
    return sum(timer_counts)


def day06a():
    return simulate_lanternfish(80)


def day06b():
    return simulate_lanternfish(256)


print(day06a())
print(day06b())
