# Python provides 47 built-in string methods attached directly to the str object
# Note: String functions are immutable i.e. their values does not change on running functions on them.

# Key String Methods 

 # * CategorizedCase & Formatting: capitalize(), casefold(), lower(), swapcase(), title(), upper().

str = "this is a string, it is an example of it."
print(str.capitalize()) # return the first letter capitilize string.
print(str.upper()) # return the string in uppercase of the string.
print(str.lower()) # return the string in lowercase of the string.
print(str.title()) #return the first letter of every word of the string in capital letters.
print(str.swapcase()) # convert the capital letters to small and small letters to capital.

text = "der fluß" # German Eszett (ß) use alt+225
# casefold: return the string to lowercase but in much more aggressive than .lower(), lower only for english alpha.
print(text.casefold()) # print der fluss.
text1 = "OΔΥΣΣΕΥΣ" 
text2 = "οδυσσεύς"
print(text1.casefold()) # oδυσσευσ
print(text2==(text1.casefold())) # false, as oδυσσευσ != οδυσσεύς


#  * Searching: count(), find(), index(), rfind(), rindex().
text = "this is the title of the poem, an example of the sentence"
print(text.count("th"))  # return the count of the given sequence in the string.
print(text.find("the"))  # return the start index of the given sequence in the string.
print(text.index("the"))  # return the start index of the given sequence in the string.
print(text.rfind("the"))  # return the last index of the given sequence in the string.
print(text.rindex("the")) # return the last index of the given sequence in the string.
# The major difference b\t .find() and.index() is:
# find(): return -1 if the substring is not found .
# index(): Raises a ValueError exception if the substring is not found.


#  * Splitting/Joining: join(), partition(), rpartition(), rsplit(), split(), splitlines().


text = "Apple Banana Orange Berry Mango"
 # split(separator,maxsplit): return tokens after given separators. default separator is whitespace. maxsplit: number of tokens after which tokenization stops
print(text.split())  # return: ['Apple', 'Banana', 'Orange', 'Berry', 'Mango']
print((text.replace(" ",',')).split(',',2)) # return: ['Apple', 'Banana', 'Orange,Berry,Mango']
# rsplit(separator,maxsplit):same as splits except it starts splitting(tokenizing) from right.if maxsplit is not used the result for both is same.
print(text.rsplit()) # return: ['Apple', 'Banana', 'Orange', 'Berry', 'Mango']
print((text.replace(" ",',')).rsplit(",",2)) # return: ['Apple,Banana,Orange', 'Berry', 'Mango']

url = "user@domain.com@extra"
# .partition(separator): Unlike split(), which can return a list of any size, these methods always return a tuple of exactly 3 elements:
# Everything before the separator.
# The separator itself.
# Everything after the separator.
print(url.partition("@")) #Return: Tuple ('user', '@', 'domain.com@extra')
print(url.rpartition("@")) #Return: Tuple ('user@domain.com', '@', 'extra')

words= ['Apple', 'Banana', 'Orange', 'Berry', 'Mango'] # List 
# connector.join(list  or tuple):exactly opposite of split() It takes an iterable (like a list or tuple of strings) and 
# glues them together into a single string, using the string it is called on as the connector.
print(" ".join(words)) #return: string Apple Banana Orange Berry Mango
print("-".join(words)) #return: string Apple-Banana-Orange-Berry-Mango

text3 = "Line1 \nLine2 \r\n Line3"
# splitlines(keepends): splits strings after linebreaks(\n,\r,\r\n), Default behaviour (Keepends = False).ie it does not includes the linebreak characters 
#  linux(\n) & windows(\r\n) endings
print(text3.splitlines()) # returns: ['Line1 ', 'Line2 \r\n', ' Line3']
print(text3.splitlines(True)) # returns: ['Line1 \n', 'Line2 \r\n\',' Line3]


# * Cleaning/Padding: center(), expandtabs(), ljust(), rjust(), lstrip(), rstrip(), strip(), zfill().
 
   # Alignment(Padding) methods:center(), ljust(), rjust(): used to pad a string to a specific TOTAL width. useful for formatting command-line menus, receipts, or text-based tables.
text = "Python"
# .center(width,fillchar): center the text and pads both the sides. Default fillchar is space(' '). Note: whitespaces comprises of (spaces,tabs,newlines).
print(text.center(12,'-')) # return: ---Python---
# .ljust(width,fillchar): Left-justifies the text and pads the right sides.
print(text.ljust(15,"*")) # return: Python*********
# .rjust(width,fillchar): Right-justifies the text and pads the left sides.
print(text.rjust(12,"."))  # return: ......Python
  
  #Cleaning methods: lstrip(), rstrip(), strip()
messy_text = " hello  \n  \rn"
# strips(chars): strips characters from both sides.Default Behaviour strips Whitespaces(spaces,tabs,newlines)
print(messy_text.strip()) # returns: hello
url = "www.bing.com"
# lstrip(chars): strips characters from the left side only.
print(url.lstrip("w."))  # returns: bing.com
# rstrip(chars): strips characters from the right side only.
print(url.rstrip(".com")) # returns: www.bing

   # Number Formatting : zfill()

# strintger.zfill(width): stands for zero fill it pads the left sides of the string with numeric zeroes.
# until it reaches the specified Total width.
print("567".zfill(5))  # returns: 00567
print("-567".zfill(5)) # returns: -0567
   # Tab Exapansion: expandtabs(tabsize)
menu = "Item\tprices"
print(menu)  # returns: Item    prices(one tab is equals to 8 spaces by default )
# expandtabs(tabsize): replaces tab characters(\t) inside a string with standard spaces. 
# By default, pythons single tab character is equals to 8 spaces.but you can pass any number you like into the method to shrink or expand the layout grid.
print(menu.expandtabs(16)) # returns: Item            prices(one tab is equals to 16 spaces is specified by us.)

#  * Modification: encode(), maketrans(), removeprefix(), removesuffix(), replace(), translate().

#encode(encoding_type): This methods converts a regular string into a byte object
text = "this is a string example just as we don't have another example."
encoded_bytes = text.encode("utf-8")
print(encoded_bytes) # returns: b"this is a string example just as we don't have another example."(The 'b' prefix means it is now bytes)
print(type(encoded_bytes)) # <class 'bytes'>

# str.maketrans(string x, string y): creates a translation lookup table mapping characters in strings x to characters in string y. Both strings must be the exact same length.
message = "hello world"
translation_table = str.maketrans("eo","30") # Creates a map: 'e' becomes '3', 'o' becomes '0'
# .translate(<translation_table>): Applies that lookup table to your string.
cipher_text = message.translate(translation_table)
print(cipher_text)

# removeprefix(substring): cuts the substring off the start if it matches.if unmatches string remains the same.
filename = "v1_final_report.pdf"
print(filename.removeprefix("v1_"))
# removesuffix(substring): cuts the substring off the end if it matches.if unmatches string remains the same
print(filename.removesuffix('.pdf'))

# replace(old_word,new_word,count): replace the count number of the old words with the new words.
txt = "you should brush your teeth regulary."
print(txt.replace("you","thou")) # returns: thou should brush thour teeth regularly
print(txt.replace("you","thou",1)) # returns: thou should brush your teeth regularly


# * Boolean Tests: isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(),
#  isnumeric(), isprintable(), isspace(), istitle(), isupper(), startswith(),endswith().

txt = 'this is a string example'
print(txt.startswith("this"))  # return true .
print(txt.endswith("ple"))  # return true.

   # Number classifications: isnumeric(), isdigit(), isdecimal()
# isdecimal(): Strictly checks for standard base-10 digits (0-9). It returns False for fractions, Roman numerals, or superscripts.
# isdigit(): Checks for standard digits plus special digit types like superscripts (e.g., ²).
# isnumeric(): The most aggressive number check. It returns True for everything isdigit() accepts, plus fractions (e.g., ½) and numerals from other languages.
# ⚠️ Note on decimals: All three methods return False if the string contains a decimal point . (like "45.6"), because the dot is a punctuation mark, not a digit character.

clean_numbers= "42"
unicode_fraction = "¾" 
print(clean_numbers.isdecimal()) # return True (base-10 digit).
print(clean_numbers.isdigit()) # return True.
print(clean_numbers.isnumeric()) # return True

print(unicode_fraction.isdecimal()) # return False (not base-10 digit).
print(unicode_fraction.isdigit()) # return False .
print(unicode_fraction.isnumeric()) # return True.

   # text and case-tests
# isalpha(): Returns True if all characters in the string are alphabetic letters (A-Z, a-z). It returns False if there are spaces, numbers, or symbols.
txt = 'amiT'
print(txt.isalpha())  # return True.
txt2 = " amit shah"
print(txt2.isalpha())  # return False, as it includes a spaces.
# isalnum(): Returns True if every character is either a letter or a number (alphanumeric). Returns False if it contains spaces or punctuation.
txt = 'Amit345'
print(txt.isalnum())  # return True.
txt2 ='amit_shah45'
print(txt2.isalnum()) # return False.
# islower(): Returns True if all cased letters in the string are lowercase. It ignores number and spaces.
txt = 'amit $5'
print(txt.islower()) # return true, here $ is uncased symbol
txt2 = "amit Δ123 "
print(txt2.islower()) # return false, as Δ is uppercase symbol.
# isupper(): Returns True if all cased letters in the string are uppercase. It ignores number and spaces.
txt = "AM145 ΣΜΔ "
print(txt.isupper())  # returns true,as Δ, Σ, Μ are uppercased symbol.
txt2= 'AM145 σμδ'
print(text2.isupper()) # returns false, as δ, σ, μ are small case letters.
print()
# istitle(): Returns True if the string follows Title Case (every word starts with an uppercase letter followed by lowercase letters)
txt ='This Is A Sentence'
print(txt.istitle())  # return True , as the sentence is in title case.
 
   # Structural & System test: isspace(), isascii(), isprintable(), isidentifier()
# isspace(): Returns True if the string consists entirely of whitespace characters (spaces, tabs \t, or newlines \n).
txt = ' \t \n   \r\n'
print(txt.isspace())  # return true as it only consists of whitespaces(spaces,tabs,newline,\t,\n,\r\n)
# isascii(): Returns True if all characters fit within the 128 standard ASCII character set (English letters, common numbers, basic punctuation).
#  It returns False for emojis or international characters like ß or é.
txt= "amit # $%^"
print(txt.isascii())  # returns True, as it only contains ascii characters.
txt2 = "amit 𝔼"
print(txt2.isascii())  # returns false, as 𝔼 is not a ascii character.
# isidentifier(): Returns True if the string can be used as a valid variable name or function name in Python 
# (i.e., it must not start with a letter or underscore, and contain only letters, numbers, or underscores).
id = "amit_123"
print(id.isidentifier()) # return whether the given string is correct identifier according to the pythons rule.
an = "234amit"
print()
# isprintable(): Returns True if all characters can be seen visually on screen. It returns False if the string contains hidden control characters like \n (newline) or \t (tab).
hidden_control = "line1 \t line2"
print(hidden_control.isprintable()) # return false , as it contain a hidden control character (\t)


# * Formatting: format(), format_map() --used for string interpolation (injecting variables dynamic values inside a text template).
   # same a printf() in java.
# format(): it allows you to inject values using either positional argument(in order) or keyword arguments(named variables
  # example 1 : positional argumeants
template = 'hello {}, your ticket number is {}.,'
print(template.format("alice",404))  # returns: hello alice, your ticket number is 404.
   # example 2: keywords arguments
template = "The {items} costs ${price}."
print(template.format(items="laptop",price=899)) #returns: Tht laptop costs $899.

#format_map(): This method is specialized. It accepts exactly one argument, which must be a dictionary (or a dictionary-like object mapping keys to values).
#  data dictionary
user_profile = {
    "username": "CodeWizard",
    "rank": "Gold"
}
# The keys match the placeholders exactly 
template = "Welcome back {username}! Current Rank: {rank}."
print(template.format_map(user_profile))  # returns: Welcome back CodeWizard! Current Rank: Gold.
  #key Comparission: format(**dict) VS format_map(dict).
'''you can use technically use standard format() with dictionaries by unpacking then using **. for example: template.format(**user_profile).

 However format_map() has two major advantages that make it distinct:
Advantage 1: It avoids creating s temporary copied dictionary: When you use .format(**my_dict), Python has to unpack the dictionary and copy it into keyword variables under the hood. 
format_map(my_dict) points directly to your existing dictionary, making it faster and more memory-efficient for massive datasets.

Advantage 2: It handles missing keys safely (Using custom Dictionaries): if a placeholder is missing from a standard dictionary, format() or format_map() will normaly crash with a KeyError .
However, because format_map() acts directly on the mapping object,
you can subclass Python's native dict to gracefully handle missing values without throwing errors.

                                   ****Strings Funtions Over*****
'''