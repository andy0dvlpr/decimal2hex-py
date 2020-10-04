integer = int(input("Decimal: "))
# The "int()" will transform the input into an integer, since in Python 3
# by default it gets picked up as a string, which breaks the thing below.
print("Hexadecimal: %x" % integer)