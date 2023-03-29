ais_minimum = float(input())

for gpa in range(30, 41):
    row_gpa = gpa / 10.0
    row_test_score = 1600.0 * (ais_minimum / 100.0) - 1600.0 * 2.5 * (row_gpa / 4.0)
    print(f"{row_gpa} {row_test_score}")
