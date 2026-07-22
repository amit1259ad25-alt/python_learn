a = input("Enter your number1: ")  # input() function is used to take input from user.
b = input("Enter your number2: ")  # input() function is used to take input from user.

print("Number a is :" ,a)  # prints the number1 entered by the user.
print("Number b is :" ,b)  # prints the number2 entered by the user.

print(a+b)  # prints the concatenation of number1 and number2 because input() function returns string type.
print()

a = int(a)
b = int(b)
print(a+b)  # prints the sum of number1 and number2 because we typecasted the string to int.