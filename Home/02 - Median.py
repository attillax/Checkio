def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
 
def bubble_sort(arr):
    i = len(arr)
    while i > 1:
       for j in range(i - 1):
           if arr[j] > arr[j + 1]:
               swap(arr, j, j + 1)
       i -= 1
    return arr

def checkio(data):
    copy = bubble_sort(data)
    if len(copy) % 2 == 1:
        middle = len(copy) / 2
        median = copy[middle]
    else :
        middle = len(copy) / 2
        median = (copy[middle] + copy[middle - 1]) / 2.0
    return median

'''#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
#    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")'''