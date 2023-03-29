"""24-hour time (also known in the U.S. as military time) is widely used around the world. Time is expressed as hours
since midnight. The day starts at 00:00, and ends at 23:59. Write a program that converts am/pm time to 24-hour time.
The input is two numbers and a string. If the input is 2 30 pm, the output should be 14:30. If the input is 12 01 am,
the output should be 00:01.
"""

hour = int(input("input the hours="))
min = int(input("input the min="))
amPm = input("input am or pm=")

if amPm == "pm":
    hour = (hour + 12) if not hour == 12 else 0
elif amPm == "am" and hour == 12:
    hour = 0

print("{:02d}:{:02d}".format(hour, min))
