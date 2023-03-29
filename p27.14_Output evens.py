"""
(1) Given positive integer n, write a for loop that outputs the even numbers from n down to 0. If n is odd, start with the next lower even number. Hint: Use an if statement and the % operator to detect if n is odd, decrementing n if so.

Enter an integer:
7
Sequence: 6 4 2 0
(2) If n is negative, output 0. Hint: Use an if statement to check if n is negative. If so, just set n = 0.

Enter an integer:
-1
Sequence: 0
"""

n = int(input("Enter integer val="))
if n > 0:
    n = (n - 1) if n % 2 == 1 else n
    seq = str(n)
    for i in range(n - 2, 0, -2):
        seq += " " + str(i)
seq += " " + str(0)

print("Sequence: ", seq)
