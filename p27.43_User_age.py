def get_age(birth_month, birth_day, birth_year, curr_month, curr_day, curr_year):
    age = curr_year - birth_year

    if age < 1:
        return 0

    if curr_month < birth_month:
        age -= 1
    elif curr_month == birth_month and curr_day < birth_day:
        age -= 1

    return age


birth_date = [int(x) for x in input("Enter birth date (month day year): ").strip().split()]
current_date = [int(x) for x in input("Enter current date (month day year): ").strip().split()]

print(get_age(*birth_date, *current_date))

