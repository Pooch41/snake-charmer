import os

print(os.listdir())
print(os.getcwd())

os.chdir('subfolder')
print(os.getcwd())
