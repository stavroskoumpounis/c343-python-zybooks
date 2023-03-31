integer_str = input("Enter a large number = ").strip()

count = 0
out_str = ""

for i in range(len(integer_str) - 1, -1, -1):
    count += 1
    out_str = integer_str[i] + out_str
    if count == 3 and i != 0:
        out_str = "," + out_str
        count = 0

print(out_str)
