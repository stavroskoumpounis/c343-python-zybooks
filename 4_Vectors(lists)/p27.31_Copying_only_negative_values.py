list_ints = [int(x) for x in input("Enter a list of 6 elements separated by spaces: ").split()]

list_negatives = [x for x in list_ints if x < 0]

print(len(list_negatives))
for x in list_negatives:
    print(x)
