import os
print("Test a path exists or not:")
path = 'C:/Users/Admin/Desktop/Lab6'
print(os.path.exists(path))
path = 'C:/Users/Admin/Desktop/Lab6'
print(os.path.exists(path))
if os.path.exists(path):
    print("\nFile name of the path: ", os.path.basename(path))
    print("\nDir name of the path: ", os.path.dirname(path))

