def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def selection_sort(array):
    n = len(array)

    for i in range(n):
        mini, minval = i, array[i]
        for j in range(i, n):
            if array[j] < minval:
                mini, minval = j, array[j]
        array[mini], array[i] = array[i], array[mini]

    return array

def insertion_sort(array):
    ret = []
    n = len(array)

    for i in range(n):
        val, ind = array[i], 0
        while ind < i and ret[ind] < val:
            ind += 1
        ret.insert(ind, val)

    return ret
        
