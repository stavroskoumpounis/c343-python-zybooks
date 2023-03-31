subset = [int(x) for x in input("Enter a list of 15 elements (0 or 1): ").split()]

chapters = []
for i, chap in enumerate(subset):
    if chap == 1:
        chapters.append(i + 1)
print(chapters)

string = ""
i = 0
while i < len(subset) - 2:
    if subset[i:i + 3] == [1, 1, 1]:
        string += str(i + 1) + "-"
        i += 3
        while i < len(subset) and subset[i] == 1:
            i += 1
        string += str(i) + " "
    elif subset[i] == 1:
        string += str(i + 1) + " "
        i += 1
    else:
        i += 1

print(string)
