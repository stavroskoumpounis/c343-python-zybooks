num = int(input("Enter a positive integer: "))

while num > 0:
    rightmost_digit = num % 10
    print(rightmost_digit)
    num = num // 10
