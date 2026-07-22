a = "45.78"
print(a)  # 45.78
t = type(a)
print(t)  # class <str>

a = float(a)  # typecasting string to float
print(a)  # 45.78

t = type(a)
print(t)  # class <float>

a = int(a)  # typecasting float to int
print(a)  # 45

type(a)  # class <int>
print(t)  # class <float>  // t is still float because we did not update it after typecasting to int.

b ='harry'
b = int(b)  # typecasting string to int will give error because string is not a number.
print(b)  # ValueError: invalid literal for int() with base 10: 'harry'
print(type(b))  # class <str>  // b is still string because typecasting to int failed.