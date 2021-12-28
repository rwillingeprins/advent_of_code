TARGET_X_MIN = 137
TARGET_X_MAX = 171
TARGET_Y_MIN = -98
TARGET_Y_MAX = -73

max_y = TARGET_Y_MIN
n_distinct_velocity_values = 0
for initial_x_velocity in range(TARGET_X_MAX + 1):
    for initial_y_velocity in range(-abs(TARGET_Y_MIN), abs(TARGET_Y_MIN)):
        x_velocity = initial_x_velocity
        y_velocity = initial_y_velocity
        x = y = 0
        while True:
            if TARGET_X_MIN <= x <= TARGET_X_MAX and TARGET_Y_MIN <= y <= TARGET_Y_MAX:
                max_y = max(max_y, initial_y_velocity * (initial_y_velocity + 1) // 2)
                n_distinct_velocity_values += 1
                break
            x += x_velocity
            y += y_velocity
            if x_velocity > 0:
                x_velocity -= 1
            elif y < TARGET_Y_MIN:
                break
            y_velocity -= 1
        if x < TARGET_X_MIN:
            break
print(max_y)
print(n_distinct_velocity_values)
