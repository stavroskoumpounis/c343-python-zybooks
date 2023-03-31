def pickup_minutes(user_x, user_y, d1_x, d1_y, d2_x, d2_y, d3_x, d3_y):
    user_d1_dist = abs(user_x - d1_x) + abs(user_y - d1_y)
    user_d2_dist = abs(user_x - d2_x) + abs(user_y - d2_y)
    user_d3_dist = abs(user_x - d3_x) + abs(user_y - d3_y)

    min_dist = min(user_d1_dist, user_d2_dist, user_d3_dist)

    return min_dist * 2


input_params = [float(x) for x in input().split()]
print(pickup_minutes(*input_params))
