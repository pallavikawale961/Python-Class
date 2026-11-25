#program for accepting two numerical value and decide biggest and check for equality also
#SimpleIfStmtEx1
a = float(input("Enter First Value:"))
b = float(input("Enter Second value:"))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(b,a,b))
if(a==b):
    print("Both the value are equal")
print("program execution completed!!")
