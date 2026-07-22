  # type(a)  return the type of variable a.

a = 56 
t = type(a) # class <int>
print(t)

b = 67.93
t = type(b)  # class <float>
print(t)

c = 'harry'
t=type(c) # class <str>
print(t)

d = False
t = type(d)  # class <bool>
print(t)

e = None 
t = type(e)  # class <NoneType>
print(t)

t =type(t)  # class <type>
print(t) 

class Myclass:
    pass

# print(Myclass.__name__)  # Myclass
# print(Myclass.__module__)  # __main__
# print(Myclass.__bases__)  # (<class 'object'>,)  // base class of Myclass is object.
# print(Myclass.__dict__)  # {'__module__': '__main__', '__init__': <function Myclass.__init__ at 0x000001F9D3A1C670>, '__dict__': <attribute '__dict__' of 'Myclass' objects>, '__weakref__': <attribute '__weakref__' of 'Myclass' objects>, '__doc__': None}  // all the attributes of class Myclass.
# print(Myclass.__doc__)  # None  // docstring of class Myclass.
# print(Myclass.__class__)  # <class 'type'>  // class Myclass is of type type.
# print(Myclass.__module__)  # __main__  // module name where class Myclass is defined.
# print(Myclass.__init__)  # <function Myclass.__init__ at 0x000001F9D3A1C670>
# print()


obj = Myclass()
t = type(obj)
print(t)    # class <__main__.Myclass>   // object are of class type.


