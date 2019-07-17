"""
The program uses a list of temperatures in degrees Celsius
Sets a variable, index, to be zero
Prints a header for a table
In the while loop which runs until the list of degrees celsius is empty
each of the item in the list:
- are assigned to C in turn
- C is put into the formula to calculate F
- the results are printed
- the index is augemented with 1
"""

Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
index = 0
print("\t C \t F")
while index < len(Cdegrees):
    C = Cdegrees[index]
    F = (9.0 / 5.0) * C + 32
    print("\t{}\t{}".format(C, F))
    index = index + 1
