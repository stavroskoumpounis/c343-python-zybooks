numbers = list(map(int, input("Enter a list of integers (space-separated): ").split()))

num_ints = numbers[0]
for i in range(1, num_ints):
    print(f"{numbers[i]}, ", end="")
print(f"{numbers[num_ints]}.")
