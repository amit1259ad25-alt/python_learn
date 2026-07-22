# replace the double-spaces from the problem string with single  spaces.

a = "this is a  string containing double spaces  in a string"
print(a.find("  "))
print(a.rfind("  "))
print(a.replace("  "," ").replace("double","single"))
print(a)  # string are immutable which means you cannot change them by running functions on them.
