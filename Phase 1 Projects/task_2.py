# Program that automatically backs up specified files or directories to a designated location in python

from datetime import date 
from shutil import copyfile

date_backup = date.today() 
print(date_backup)

str_date_backup = str(date_backup).replace('-','.') 
print(str_date_backup)

path_input = r'___' #Enter the source file path

path_output = r'___' '''Comment -> Enter path of the designation folder where you want to backed up your files''' + '\\' + str_date_backup + ' -  ' # Enter name for the backed up file 
print(path_output)

copyfile(path_input, path_output)