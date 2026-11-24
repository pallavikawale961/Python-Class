# Program for accepting a value and decide weather it is palindrome
value = input("Enter a value:")
print("given value:", value)
res = "Palindrome" if value == value[::-1] else "NOT Palindrome"
print("{} is {}".format(value,res))