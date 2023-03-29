list_ints = [int(x) for x in input("Enter a list of 10 elements separated by spaces: ").split()]

mini = list_ints[0]
maxi = mini
sum_ = 0

for x in list_ints:
    if x > maxi:
        maxi = x
    if x < mini:
        mini = x
    sum_ += x

print(mini, maxi, sum_/len(list_ints))
