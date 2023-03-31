list_size = int(input())
num_list = list(map(int, input().split()))
is_sorted = True

for i in range(1, list_size):
    if num_list[i] < num_list[i-1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Unsorted")
