"""
A state's Department of Motor Vehicles needs a program to generate license plate numbers. A license plate number
consists of three letters followed by three digits, as in CBJ523. (So "number" is a bit inaccurate, but that's the
standard word used for license plates). The plate numbers are given out in sequence, so given the current number,
the program should output the next number. If the input is CBJ523, the output should be CBJ524. If the input is
CBJ999, the output should be CBK000. For the last number ZZZ999, the next is AAA000.
"""

plate_num = input()
letters = plate_num[:3]
digits = plate_num[3:]

if digits == "999":
    if letters == "ZZZ":
        letters_next = "AAA"
    else:
        first_letter = chr(ord(letters[2]) + 1)
        if first_letter == "[":
            first_letter = "A"
            third_letter = letters[0]
            second_letter = chr(ord(letters[1]) + 1)
            if second_letter == "[":
                second_letter = "A"
                third_letter = chr(ord(letters[0]) + 1)
        else:
            second_letter, third_letter = letters[1], letters[0]

        letters_next = third_letter+second_letter+first_letter
    digits_next = "000"
else:
    digits_next = str(int(digits) + 1).zfill(3)
    letters_next = letters

new_plate = letters_next + digits_next
print(new_plate)