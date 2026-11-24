a = int(input("Enter a value of a:"))
b = int(input("Enter a value of b:"))
res = a if a>b else b if b>a else "Equal"
print(res)