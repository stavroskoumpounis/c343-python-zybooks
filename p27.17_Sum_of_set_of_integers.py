while True:
    num_of_ints = int(input("Enter the number of integers: "))
    if num_of_ints <= 0:
        break

    total_sum = 0
    for i in range(num_of_ints):
        num = int(input(f"Enter int {i + 1}: "))
        total_sum += num

    print("Sum: ", total_sum)
