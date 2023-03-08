string = input()
upp = 0
low = 0
for i in string:
    if i.isupper():
        upp += 1
    else:
        low += 1
 
print("number of upper case: ", upp)
print("number of lower case: ", low)