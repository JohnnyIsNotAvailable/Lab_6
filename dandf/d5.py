list = ['zxcc', 'asd', 'qwerty', 'fgh']
with open('test.txt', "w") as txtfile:
        for item in list:
                txtfile.write("%s\n" % item)

ans = open('test.txt')
print(ans.read())