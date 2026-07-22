# write a program to dectect double-spaces in a string.
a = "this is a  string containing double spaces  in a string"
print(a.find("  "))
print(a.rfind("  "))