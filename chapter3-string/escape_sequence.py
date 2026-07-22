#  Escape Sequences in python: Sequence of characters after backslash "\", 
# it comprises of more than one character but represent one character when used within the strings.

# null - Ascii 0.  total ascii character equals to 128,(256 extended) further extended by unicode range.
# \    - Line Continuation, joins two lines of codes together(this is a compiler instruction, not a character to tell python that a single line of code is continuing on the next line.).
# \a   - Bell(Ascii 7), makes a terminal alert or beep sound)
# \b   -  Backspace(Ascii 8), moves the cursor back one character.
# \t   - Horizontal Tab(Ascii 9), for tabs of 8 spaces(default)
# \n   - Line Feed(Ascii 10), move the cursor to  nextline(standard linux/mac-os newline) .
# \v   - Vertical Tab(Ascii 11), inserts vertical spacing.
# \f   - Form Feed(Ascii 12), forces a page break in some printers\terminal.
# \r   - Carriage Return(Ascii 13), Return the cursor to the beginning of the line.
# \r\n - Carriage Return(CR), Resets cursor and moves to a new line.(standard windows/http newline).
# \"   - Double-quote(")[Ascii 34] in a double quoted string.
# \'   - Single-quote(')[Ascii 39] in a single quoted string.
# \\   - Backslash(\)[Ascii 92] in a string.
# \N{name} - Named Unicode character(looks up character by name, e.g, \N{GREEK CAPITAL LETTER DELTA})
# \ooo - Octal Notation represent octal value, Ascii symbol(\101 for A).
# \xhh - Hexadecimal Notation represent hexa value, Ascii symbol(\x41 for a)
# \uxxxx -16 bit Hex-Unicode character .
# \uxxxxxxx - 32 bit Hex-Unicode character.
print('This will be printed \
as a single Line.')
# This will be printed as a single Line.
print("This is Line1\nThis is Line2") 
# This is Line1
# This is Line2
print("This is a string\tHere we are leaving a tab space")
# This is a string        Here we are leaving a tab space
print("<overwritten> write the character of 13 letters\rwellington is")
# wellington is write the character of 13 letters
print("Line1\r\nLine2")
# Line1
# Line2
print("My name is: \"Amit\' \\")
# My name is: "Amit' \
print("produce a beep sound \a .")
# we can't hear beep sound in python ide or vs-code because notification are in-build off in them, instead we can use power
print("printing greek capital delta \N{GREEK CAPITAL LETTER DELTA}")
#printing greek capital delta Δ
print("it will edit the last letter\bℝ")
# it will edit the last letteℝ
print("Testing\vVertical Spacing")
# Testing
#        Vertical Spacing
print("Ascii symbol for octal value 101 is \101")
# Ascii symbol for octal value 101 is A
print("Ascii symbol for hexa value F6 is \xF6")
# Ascii symbol for hexa value 56 is ö
print("Unicode character for 4 digit hex value b123 is \ub123")
# Unicode character for 4 digit hex value a123 is  넣

# Δ Python uses a feature called Universal Newline Support.
#  When you read or write files using open(), Python automatically translates \r\n (Windows) into \n while reading,
#  and translates \n back to the host system's native format (\r\n on Windows) when writing.

# Δ How to Ignore Escape Sequences
# you can disable escape sequence interpretation entirely by prefixing the string with an r or R.This creates a raw string:
# Normal string interprets \n as a newline
print("C:\new_folder\test.txt") 

# Raw string treats backslashes as regular characters
print(r"C:\new_folder\test.txt") 