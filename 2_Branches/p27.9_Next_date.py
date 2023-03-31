"""Many websites let users make reservations (hotel, car, flights, etc.). When a user selects a date, the next day is
often automatically selected (for hotel checkout, car return, flight return, etc.). Given a date in the form of three
integers, output the next date. If the input is 1 15 2017, the output should be 1 16 2017. If the input is 8 31 2017,
the output should be 9 1 2017. Ignore leap years.
"""

month = int(input("Enter month:"))
day = int(input("Enter day:"))
year = int(input("Enter year:"))

if month == 2:
    month_days = 28
elif month in [4, 6, 9, 11]:
    month_days = 30
else:
    month_days = 31

if day < month_days:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print(f"{month} {day} {year}")
