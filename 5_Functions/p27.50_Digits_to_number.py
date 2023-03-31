def digits_to_number(digits):
    total_value = 0
    multi = 1

    for digit in digits:
        total_value += digit * multi
        multi *= 10

    return total_value


digits = [9, 6, 2]
result = digits_to_number(digits)
print(result)
