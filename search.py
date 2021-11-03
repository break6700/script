# Search's for simple

# Import OS
import os

# Indicate search path
path = input('ENTER YOUR DIRECTORY PATH (LEAVE EMPTY TO SEARCH CURRENT DIRECTORY): ')
file_type = input('PLEASE ENTER FILE TYPE: ')
term = input('PLEASE ENTER THE SEARCH TERM: ')

# Check if file path exists
if not os.path.exists(path):
            path ="."

# return list of files in path
directory = os.listdir(path)

# 
for file in directory:
    if file.endswith(file_type):
        with open(file) as f:
            if term in f.read():
                print(file)


