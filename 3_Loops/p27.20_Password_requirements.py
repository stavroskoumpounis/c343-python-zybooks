def password_requirements(password):
    has_min_length = len(password) >= 8
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in "!#%" for c in password)

    if has_min_length and has_letter and has_number and has_special:
        print("OK")
    else:
        if not has_min_length:
            print("Too short")
        if not has_letter:
            print("Missing letter")
        if not has_number:
            print("Missing number")
        if not has_special:
            print("Missing special")


input_password = input("Enter a password: ")
password_requirements(input_password)
