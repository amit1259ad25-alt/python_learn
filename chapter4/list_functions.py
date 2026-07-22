# Python provides 11 built-in list methods to directly modify and interact with lists,
#  along with several built-in global functions that accept lists as arguments
 
# Built-in list methods (11 list methods)
# append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()

friends = [ "Apple","Oranges",5, 456.35,False,None,"Aakash","rohan"]
# append(item): Adds a single element to the very end of the list, append means: add to end 
friends.append("amit")   
print(friends) #  ['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'amit']
# extend(iterable): Adds add elements from another iterable (like a list,tuples or string) to the list.
s = "ok"
friends.extend(s)
print(friends)  # ['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'amit', 'o', 'k']
t = ("amit",76,"place")
friends.extend(t)
print(friends) # ['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'amit', 'o', 'k', 'amit', 76, 'place']
# insert(idx,item): Adds a single element at a specified position or index.
friends.insert(3,"the")
print(friends) # ['Apple', 'Oranges', 5, 'the', 456.35, False, None, 'Aakash', 'rohan', 'amit', 'o', 'k', 'amit', 76, 'place']
# remove(item): Removes the first occurence of a specified values from the list.
friends.remove("amit")
print(friends) # ['Apple', 'Oranges', 5, 'the', 456.35, False, None, 'Aakash', 'rohan', 'o', 'k', 'amit', 76, 'place']
# pop(index): Removes and returns the element at a given index (defaults to the last item)
friends.pop()       # default remove from the last.
print(friends) # ['Apple', 'Oranges', 5, 'the', 456.35, False, None, 'Aakash', 'rohan', 'o', 'k', 'amit', 76]
friends.pop(3)       # remove from the third index position .
print(friends) # ['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'o', 'k', 'amit', 76]
# clear(): Removes and returns all elements, leaving the list completely empty.
friends.clear()
print(friends) # []
# index(item): Returns the index position of the first occurence of a specific value from the list.
friends =['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'o', 'k', 'amit', 76]
print(friends.index("amit"))  # 10
# sort(): Sorts the original list items in ascending or descending orders in-place .
st = ["sunita","shalini","amit","pratibha",'sunil']
st.sort()      # For this list should either be string or decimals but not the combinations of both.
print(st) # ['amit', 'pratibha', 'shalini', 'sunil', 'sunita']
# reverse(): Reverse the ordes of the elements in the original list-in-place.
st.reverse()
print(st) # ['sunita', 'sunil', 'shalini', 'pratibha', 'amit']
# copy(): Return a shallows copy of the entire list.
l= st.copy()     # copies the values of the  list.
print(l) # ['sunita', 'sunil', 'shalini', 'pratibha', 'amit']

# Built-in Global Functions for lists
# Aside from 11 methods above, python also provides 6 global built-in functions that commonly accept a list as an argument
# len(list), max(list),min(list), sum(list), sorted(list), list(list) 
# dir(list): used in powershell to know the functions of pythons .

# len(list): Returns the total numbers of items in the list.
friends =['Apple', 'Oranges', 5, 456.35, False, None, 'Aakash', 'rohan', 'o', 'k', 'amit', 76]
st = ["mango","banana","oranges","grapes","Apples"]
print(len(st))

# max(list): Returns the largest item in the list.
print(max(st))

# min(list): Returns the smallest item in the list.
print(min(st))

# sum(): Adds up all numerical items in the list returns the total.
el = [34,23,56,67,34,67,90.89]
print(sum(el))

# sorted(list): Returns a new sorted list without changing the originals one. 
new = sorted(el)
print(new)

# list(iterable): Converts another data type(like a tuple or string or dictionary) into a list.

# String to list
s = "amit shah"
chars = list(s)
print(chars) # ['a', 'm', 'i', 't', ' ', 's', 'h', 'a', 'h']

# tuple to list 
num = list((1,2,3))
#  Alt, num  = list(range(3))
print(num)

# set to tuple 
unique_items = list({1,3,3,5,7})  # remove the duplicate items, order become random become random.
print(unique_items) # [1,3,5,7]

# dictanaries to list
d = { 
    "key": "value",
    "place":"Jantar mantar"
}
ls = list(d)  # extracts only keys.
print(ls) # ['key', 'place']

# making independent copies
copy = list(ls) 
print(copy) # ['key', 'place']

# creating empty list 
ls = list()
print(ls) 

