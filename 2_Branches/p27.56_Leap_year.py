year = int(input())

is_leap = False
if year % 4 == 0:
    is_leap = True
if year % 100 == 0 or year % 1000 == 0:
    is_leap = True if year % 400 == 0 else False

print(is_leap)
