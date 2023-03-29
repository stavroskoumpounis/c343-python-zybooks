yearlyValues =[int(x) for x in input("Enter a list of elements separated by spaces: ").split()]
n = len(yearlyValues)
for x in range(0, n-1, 4):
    print(yearlyValues[x], yearlyValues[x+1], yearlyValues[x+2], yearlyValues[x+3])
