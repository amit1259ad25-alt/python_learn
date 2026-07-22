# Write a program to fill in a template given below with name and date.

letter = '''
            Dear <|Name|>
            You are selected!
            <|Date|>
            '''
print(letter.replace("<|Name|>","Amit").replace("<|Date|>","21\\07\\2026"))
# ALT
template = '''
           Dear {Name}
            You are selected!          
           {Date}
            '''
print(template.format(Name ="Amit Shah",Date = "22\\07\\26"))

# alt 
Name =input("Enter your name:")
Date =". 22\\07\\26"
print(f'''
           Dear {Name}
            You are selected!          
           {Date}
            ''')