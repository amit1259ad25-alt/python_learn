# write a program to print the contents of a directory using the os module .search online for the function that do that.


import os 

# specify the directory you want to list 
directory_path = "C:\\Users\\Amit Shah\\OneDrive\\Desktop\\branch_merge"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name.
for item in contents:
    print(contents)


