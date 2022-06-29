array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
def twon(array,sequence):
    arr = 0
    seq = 0
    while arr <= len(array) and seq <= len(sequence):
        if array[arr] == sequence[seq]:
            seq += 1
        else:
            arr += 1
    



twon(array, sequence)