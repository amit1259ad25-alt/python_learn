# A string in python is sliced for getting a part of the strings.

name  = 'Harry' # indexing starts from zero to (length-1), in this case last index is 4.


# Slicing(Substring) & Character at an index.  Syntax: sl = name[idx_start:idx_End]  & ca = name[idx]
slicename = name[0:3]  # same as subString(first idx,last idx): return the subString not including the last index. 
print(slicename)
print(name[:3])  # equals to: name[0:3]
print(name[1:])   # equals to: name[1:last_idx(len-1)]

ca = name[1]  # same charAt(): returns the char at given index of string.
print(ca)

# Negative slicing ,indexing starts from -1.
name2 = "Harry"
print(name2[-4:-1])    # -4 included but -1 not included .
print(name2[1:4])
print(name2[-10:-1])
print(name2[1:10])

# Slicing with skip value
word = "amazing"
print(word[1:6:2])   # "mzn"   skips every second word from the sliced String.(Here skip value is 2).

