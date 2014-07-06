# -*- coding: utf-8 -*-
def checkio(text):
    dict1 = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    for i in range(len(text)):
        a = text[i]
        if a in 'abcdefghijklmnopqrstuvwxyz':
            dict1[a] += 1
        if a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            b = a.lower()
            dict1[b] += 1
    d = max(dict1.values())

    for key, value in dict1.items():
        if value == d:
                res = key
                break
    return res 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")