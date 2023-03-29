binary_str = input("Enter a binary number: ")
binary_list = [int(x) for x in binary_str]
n = len(binary_list)

decimal = 0
for i, x in enumerate(reversed(binary_list)):
    decimal += x * (2 ** i)

print(decimal)
