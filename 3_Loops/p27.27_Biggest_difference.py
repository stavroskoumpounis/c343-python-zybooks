list_size = int(input())
prev_num = int(input())
max_diff = 0

for i in range(1, list_size):
    curr_num = int(input())
    curr_diff = abs(curr_num - prev_num)
    if curr_diff > max_diff:
        max_diff = curr_diff
    prev_num = curr_num

print(max_diff)
