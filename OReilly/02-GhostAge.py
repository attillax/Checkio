def fib(num):
    res = [0]
    f1 = 0
    f2 = 1
    for i in range(num+1):
        if (i == (f1+f2)) and (i>0):
            res.append(i)
            f1 = f2
            f2 = i
    return res

def checkio(opacity):
    age = 0
    interval = 0
    helper = 0
    a = True
    interval = 10000 - opacity
    row = fib(interval)
    for i in range(10000):
        if i in row:
            helper += i
        else:
            helper -= 1
        if helper == interval:
            age = i
            break
    return age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"

'''print checkio(10000) #0
print checkio(9999) #1
print checkio(9997) #2
print checkio(9994) #3
print checkio(9995) #4
print checkio(9990) #5
print checkio(6736) #3516'''
