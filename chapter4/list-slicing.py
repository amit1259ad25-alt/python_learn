 # list are sliced just as strings. 
friends = [ "Apple","Oranges",5, 456.35,False,None,"Aakash","rohan"]
print(friends[:3]) # ['Apple', 'Oranges', 5]  index 3 is  not included .
print(friends[2:5])

# Element at an index can be found by  :
print(friends[4])  # False

# Negative slicing ,indexing starts from -1.
print(friends[-5:-2])  # in this case -2 is not is included.

# # Slicing with skip value 
print(friends[2::2])  # skips every second value .
