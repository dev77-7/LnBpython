import shutil
a=input('Enter source path to copy:- ')
b=input('Enter destination path:- ')
shutil.copy(a,b)
print("File pasted to destination successfully!")