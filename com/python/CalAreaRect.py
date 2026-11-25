# Program for calculating area and circumference of rectangle
length = float(input("Enter Length:"))
breadth = float(input("Enter Breadth:"))
#call area
ar = length * breadth
# cal circumference
cr = 2 * (length + breadth)
print("="*20)
print("length={}". format(length))
print("breadth={}".format(breadth))
print("area of rect={}". format(ar))
print("circumference of rect={}". format(cr))
