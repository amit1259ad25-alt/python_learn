# Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry, this python course in nice. Thanks!"
print(letter)
letter = letter[0:letter.find(",")+1]+"\n"+"\t" +letter[letter.find(",")+2:letter.find(".")+1]+"\n"+ letter[letter.find(".")+2:]
print(letter)

