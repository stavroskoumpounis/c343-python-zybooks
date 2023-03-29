list_ints = [int(x) for x in input("Enter a list of 10 elements separated by spaces: ").split()]
int_dict = {}

for x in list_ints:
    if x < 0 or x > 99:
        print(f"Invalid input: {x} is not in 0-99")
        exit(0)

    if x not in int_dict.keys():
        int_dict[x] = 1
    else:
        int_dict[x] += 1

if int_dict:
    max_key = max(int_dict, key=int_dict.get)
    max_value = int_dict[max_key]
    print(max_key, max_value)
