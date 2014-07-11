FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    temp = number
    res = ''
    #check if 1XX - 9XX
    if temp >= 100: 
        if (temp/100 > 0) and (temp/100 < 10):
            res += FIRST_TEN[temp/100-1]+' '
        res += HUNDRED
        temp = temp%100
        if temp > 0:
            res += ' '
    #check if 2X-9X
    if (temp <= 99) and (temp >= 20):
        res += OTHER_TENS[(temp-20)/10]
        temp = temp%10
        if temp > 0:
            res += ' '
    #check if 10-19
    if (temp >= 10 ) and (temp < 20):
        res += SECOND_TEN[temp-10]
    #check if 1-9
    if (temp <= 9) and (temp != 0):
        res += FIRST_TEN[temp-1]
    return res

'''if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"'''
