# Import python libraries
import os

# Get current working directory
cwd = os.getcwd()

DEMO_FILES = 'trainer_demo_files/demo_files'

# Exercise 1 - reading a file w/ try & except

# Store file path in a variable
file_path = os.path.join(cwd, DEMO_FILES, 'data.txt')

# Open and read the file
try: 
    file = open(file_path)
    file_content = file.read()
    file.close()
    print(file_content)
except FileNotFoundError:
    print('File does not exist!')

