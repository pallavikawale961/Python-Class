#program for accepting two numerical value and decide biggest and check for equality also
#IfElseStmtEx1
a = float(input("enter first value:"))
b = float(input("Enter second value:"))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
else:
    print("Big({},{})={}".format(a,b,b))
print("program execution completed")
