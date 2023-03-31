def digit_to_word(digit):
    digit_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                  9: "nine"}

    return digit_dict[digit] if 0 <= digit <= 9 else "error"


def tens_digit_to_word(digit):
    digit_tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                       9: "ninety"}

    return digit_tens_dict[digit] if 2 <= digit <= 9 else "error"


def two_digit_num_to_words(number):
    number_word = tens_digit_to_word(number // 10)
    if number_word == "error":
        return "error"
    number_word += " " + digit_to_word(number % 10)
    return number_word


number_inpt = int(input("Enter 2 dig number "))

print(two_digit_num_to_words(number_inpt))