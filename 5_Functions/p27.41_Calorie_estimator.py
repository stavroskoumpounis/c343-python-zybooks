def activity_calories(activity: str, minutes: int):
    cals_act_dict = {"sit": 1.4, "walk": 5.4, "run": 13.0, "bike": 6.8, "swim": 8.7}
    return cals_act_dict[activity] * minutes


activ = input("Enter activity = ")
minutes = int(input("Enter duration in minutes = "))

print(activity_calories(activ, minutes))
