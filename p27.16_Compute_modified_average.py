validCount = 0
invalidCount = 0
sumValid = 0
userInt = int(input())
while userInt != 0:
    if userInt >= 2 and userInt <= 12:
        validCount += 1
        sumValid += userInt
    else:
        invalidCount += 1
    userInt = int(input())
if validCount > 0:
    average = float(sumValid) / validCount
    print("Average:", average)
else:
    print("Average: 0")
print("Valid:", validCount)
print("Invalid:", invalidCount)
