import os.path

file_name = 'test.txt' #input('Enter a filename:')
old_string = 'morning' #input('Enter the old string to be replaced:')
new_string = 'midnight' #input('Enter the new string to replace the old string:')

file = open(file_name,'r')
    
filedata = file.read()
file.close()

newdata = filedata.replace(old_string, new_string)

with open(file_name, 'w') as file:
    file.write(newdata)