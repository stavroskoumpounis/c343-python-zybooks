"""
A user inputs the name of a shape (square or triangle). The program outputs the shape using asterisks. For input
square, the output is:
***
* *
***
If the input is triangle, the output is:

  *
 * *
*****
"""

shape = input("Input the name of a shape (square or triangle): ")

if shape == "square":
    print(3 * "*")
    print("* *")
    print(3 * "*")
elif shape == "triangle":
    print("  *  ")
    print(" * * ")
    print(5 * "*")
else:
    print("Invalid input")
