input_str, idx, substring = input("Enter your string, index, and substring (separated by spaces): ").split()

found = -1
for i in range(int(idx), len(input_str) - len(substring) + 1):
    match = True
    for j in range(len(substring)):
        if input_str[i+j] != substring[j]:
            match = False
            break
    if match:
        found = i
        break

print(found)
