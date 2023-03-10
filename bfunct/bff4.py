import time

def sleep(num, milisec):
    time.sleep(milisec / 1000)
    return (num ** 0.5)

print("Sample input:")
num = int(input())
milisec = int(input())

ans = int(sleep(num, milisec))
print(f'Square root of {num} after {milisec} miliseconds is {ans}')

 