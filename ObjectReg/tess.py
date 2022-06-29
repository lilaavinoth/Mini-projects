counter = 0
num = int(input("Enter a number: "))
while num != 0:
    if (num % 2) == 0:
        num = num/2
        counter += 1
    else:
        num = num-1
        counter += 1
    if (num == 0):
        print(counter)
        break