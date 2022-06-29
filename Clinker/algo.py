array = [1, 2, 3, 4, 2, 3, 5, 3, 6, 3]

count = 0


customerDictonary = {
    "repeatedCustomer" : 0,
    "count" : 0
}


for i in range(len(array)):
    firstIteration = array[i]
    for wq in range(i + 1, len(array)):
        secondIteration = array[wq]
        if firstIteration == secondIteration:
            customerDictonary["count"] += 1
            customerDictonary["repeatedCustomer"] = firstIteration
            print(customerDictonary["repeatedCustomer"])
