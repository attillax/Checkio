def split_list(items: list) -> list:
    #result=[]
    if len(items) == 0:
        result = [[],[]]
    
    if len(items) == 1:
        result = [items,[]]
    if len(items) == 3:
        result = [items[0:(round(len(items)/2))],items[(round(len(items)/2)):(len(items)+1)]]   
    elif len(items) % 2 == 1:
        result = [items[0:(round(len(items)/2)+1)],items[(round(len(items)/2)+1):(len(items)+1)]]
    else :
        result = [items[0:(round(len(items)/2))],items[(round(len(items)/2)):(len(items)+1)]]
   
    return result


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")