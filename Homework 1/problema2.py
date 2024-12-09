def common_prefix(string1, string2):
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        if string1[i] != string2[i]:
            return string1[:i] # ritorna alla prima differenza tra le stringhe
    return string1[:min_len] # ritorna la tringa più piccola se non vengono trovate differenze 

def longest_prefix(strings, first, last):
    if first == last:   # caso base 1 stringa
        return strings[first] # ritorna l'intera
    
    elif last - first == 1: # caso base 2 stringhe
        return common_prefix(strings[first], strings[first+1] )# ritorna il prefisso in comune

    else:
        mid = (first + last) // 2 # dividi l'insieme in due metà
        left_strings = longest_prefix(strings, first, mid)
        right_strings = longest_prefix(strings, mid+1, last)
        return common_prefix(left_strings, right_strings)

def test_func(strings, result): # funzione per il testing
    prefix = longest_prefix(strings, 0, len(strings)-1)
    if prefix == result:
        return True
    else:
        return False

if __name__ == '__main__':

    strings_test0 = ['apple', 'ape', 'april', 'applied']
    strings_test1 = ['first', 'first']
    strings_test2 = ['algorithms', 'and', 'data', 'structures']
    strings_test3 = ['test', 'testing', 'tested']
    strings_test4 = ['element']

    print('\n')

    print('[TEST CASE 0] Testing strings: ' + str(strings_test0))
    if test_func(strings_test0, 'ap'):
        print('Result: success')
    else:
        print('Result: failed')

    print('\n[TEST CASE 1] Testing strings: ' + str(strings_test1))
    if test_func(strings_test1, 'first'):
        print('Result: success')
    else:
        print('Result: failed')

    print('\n[TEST CASE 2] Testing strings: ' + str(strings_test2))
    if test_func(strings_test2, ''):
        print('Result: success')
    else:
        print('Result: failed')

    print('\n[TEST CASE 3] Testing strings: ' + str(strings_test3))
    if test_func(strings_test3, 'test'):
        print('Result: success')
    else:
        print('Result: failed')

    print('\n[TEST CASE 4] Testing strings: ' + str(strings_test4))
    if test_func(strings_test4, 'element'):
        print('Result: success')
    else:
        print('Result: failed')

    print('\n')
