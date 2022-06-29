array = [5, 1, 22, 25, 6, -1, 8, 10]
target = [1, 6, -1, 10]
def twon(array,target):
    full = 0
    for ew in range(len(array)):
        number = array[ew]
        for eq in range(len(target)):
            sec = target[eq]
            if number == sec:
                full += 1
                if full == len(target):
                    print('complete')

twon(array,target)

for value in array:
    print(value)
for eer in range(4,6):
    print(eer)