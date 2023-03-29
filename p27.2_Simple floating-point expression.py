"""
Write an assignment statement for the following mathematical equation:

y = (1/3)x + (x/4) + 2x

Keep x as an integer. Use an expression that matches the equation's right side as closely as possible. If the input
is -1, the output is -2.58333.
"""

x = int(input("Enter x="))

y = (1.0 / 3) * x + (x / 4.0) + 2 * x

print(y)