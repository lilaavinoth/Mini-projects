array = [5, 1, 22, 25, 6, -1, 10]
sequence = [5, 1, 22, 8, 10]

initialvalue = 0

def runer(initialvalue):
    for i in range(len(sequence)):
        checker1 = sequence[i]
        for j in range(len(array)):
            checker2 = array[j]
            if checker1 == checker2:
                initialvalue += 1
            if initialvalue == len(sequence):
                return len(sequence)


print(runer(initialvalue))