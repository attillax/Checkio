VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
c = '0123456789'
a = VOWELS.lower()
b = CONSONANTS.lower()
d = a+b+c

def checkio(text):
    tt = text.lower()
    words = []
    start = 0
    for i in range(len(tt)):
        if (not(tt[i] in d) and (tt[i-1] in d)):
            end = i
            words.append(tt[start:end])
        elif (i == (len(tt)-1) and (tt[i-1] in d)):
            words.append(tt[start:len(tt)])
        if (not(tt[i-1] in d) and (tt[i] in d)):
            start = i
    wt = []
    for w in words:
        flag = 0
        for i in w:
            if i in c:
                flag = 1
        if flag == 0:
            wt.append(w)
    res = 0
    for w in wt:
        check = len(w)*'vc'
        count = ''
        for i in w:
            if i in a:
                count += 'v'
            if i in b:
                count += 'c'
        if (count in check) and (len(w) > 1):
            res += 1
    return res

'''#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"'''

checkio("1st 2a ab3er root rate")
