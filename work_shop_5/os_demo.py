import os

files = os.listdir('.')
print(files) # list all files in the current directory

path_exists = os.path.exists('file1.txt')
print(path_exists) # check if the file exists

os.mkdir('new_folder') # create a new folder