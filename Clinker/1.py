array = [-10, -5, 0, 5, 10]
newarray = []
temp = 0

def myfunction(array):
    for i in range(len(array)):
        currentvalue = array[i]
        newarray.append(currentvalue * currentvalue)

    for j in range(len(newarray)):
        for k in range(j + 1, len(newarray)):
            if newarray[j] > newarray[k]:
                temp = newarray[k]
                newarray[k] = newarray[j]
                newarray[j] = temp

    return newarray

print(myfunction(array))