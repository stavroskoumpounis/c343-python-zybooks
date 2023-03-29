num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

max = num_list[0]
for k in num_list:
    if k > max:
        max = k

print(f"The max in {num_list} is {max}")