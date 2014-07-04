def checkio(data):
    counter = ''
    for i in range(len(data)):
        if data[i] in 'abcdefghijklmnopqrstuvwxyz':
            counter += 'a'
        if data[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            counter += 'b'
        if data[i] in '0123456789':
            counter += 'c'
    if ((('a' in counter) and ('b' in counter)) and (('c' in counter) and (len(data) >= 10))):
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example" 