with open('1.txt', 'r') as first, open('2.txt', 'a') as second:
    for line in first:
         second.write(line)