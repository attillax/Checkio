def checkio(data):
    res = ''
    temp = data
    #check 1XXX-3XXX
    if temp/1000 > 0:
        res += temp/1000*'M'
        temp = temp%1000
    #check 1XX-1000
    if ((temp < 1000) and (temp >= 100)): 
        if (temp > 500):
            if (temp >= 900):
                res += 'CM'
            else:
                res += ('D'+((temp-500)/100)*'C')
        elif (temp < 500):
            if (temp < 400):
                res += (temp/100)*'C'
            else:
                res += 'CD'
        else:
            res +='D'
        temp = temp%100
    #check 1X-100
    if ((temp <= 100) and (temp >= 10)): 
        if (temp > 50):
            if (temp == 100):
                res += 'C'
            if (temp >= 90):
                res += 'XC'
            else:
                res += ('L'+((temp-50)/10)*'X')
        elif (temp < 50):
            if (temp < 40):
                res += (temp/10)*'X'
            else:
                res += 'XL'
        else:
            res +='L'
        temp = temp%10
    #check 1-10
    if (temp < 10):
        if (temp > 5):
            if (temp == 9):
                res +='IX'
            else:
                res += ('V'+(temp-5)*'I')
        elif (temp < 5):
            if (temp == 4):
                res +='IV'
            else:
                res += (temp)*'I'
        else:
            res +='V'
    return res

'''if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888' '''
