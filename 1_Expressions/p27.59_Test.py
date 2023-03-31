final_weight = 0.4

curr_grade = int(input("Enter current grade :"))

weighted_curr_grade = curr_grade * 0.6

grade_needed = 90 - weighted_curr_grade


print(f"Grade needed to get an A: {grade_needed/final_weight}")
