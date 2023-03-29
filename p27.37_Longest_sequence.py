input_string = input("Enter a list as a string: ").strip()
print(input_string)
substrings = input_string[2:].split("I")
items = []

for s in substrings:
    s = s.strip()
    items.append([x for x in s.split()])


longest_seq = max(items, key=len)
print(len(longest_seq))
