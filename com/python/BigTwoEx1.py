# program for finding Biggest of two numbers
a = int(input("Enter a value of a:"))
b = int(input("Enter a value of b:"))
# finding big of a and b
bv = b if b > a else a    # Python ternary operator
print("Big ({} , {}) = {}". format(a, b, bv))
