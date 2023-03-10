import os

for dirpath, dirnames, dirfiles in os.walk('/Users/Admin/Desktop/Lab6'):
    print("Current Path", dirpath)
    print("Direcories", dirnames)
