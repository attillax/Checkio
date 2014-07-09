VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
a = VOWELS.lower()
b = CONSONANTS.lower()

def slice(text):
    tt = text.lower()
    words = []
    start = 0
    for i in range(len(tt)):
        if (not((tt[i] in a) or (tt[i] in b)) and ((tt[i-1] in a) or (tt[i-1] in b))):
            end = i
            words.append(tt[start:end])
        elif ((i == (len(tt)-1) and ((tt[i-1] in a) or (tt[i-1] in b)))):
            words.append(tt[start:len(tt)])
        if (not((tt[i-1] in a) or (tt[i-1] in b)) and ((tt[i] in a) or (tt[i] in b))):
            start = i
    return (words)

def checkio(text):
    words = slice(text)
    print words

'''
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human" '''

checkio("My name is ...")
checkio("Hello world")
checkio("A quantity of striped words.")
checkio("Dog,cat,mouse,bird.Human.")
checkio("dfghj werty ertyui werty")
