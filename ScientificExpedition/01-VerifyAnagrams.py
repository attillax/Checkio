def make_list(word):
    res = []
    lowstr = 'abcdefghijklmnopqrstuvwxyz'
    temp = word.lower()
    for t in temp:
        if t in lowstr:
            res.append(t)
    a = sorted(res)
    return a

def verify_anagrams(first_word, second_word):
    w1 = make_list(first_word)
    w2 = make_list(second_word)
    return w1 == w2

'''if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002" '''
