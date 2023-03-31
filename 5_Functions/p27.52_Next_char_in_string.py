input_str, idx, char = [x for x in input("input your string, index and char = ").split()]

found = -1
for i in range(int(idx), len(input_str)):
    if input_str[i] == char:
        found = i
        break

print(found)


