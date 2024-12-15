def find_coins(V: int, coins: list[int]) -> int:

    n = len(coins)
    if n == 0 or V < 0: # controllo su boundary values
        return -1

    memo = {}   # dizionario per memoizzare risultati già valutati
    
    def find_min_num_coins(cost):
        
        if cost == 0:   # caso base
            return 0 
        
        if cost in memo: # se è già stato calcolato il risultato per arrivare al costo corrente
            return memo[cost]   # restituiscilo
        
        num_coins = float('inf')    # valori sentinella
        min_greater_cost = float('inf')

        for coin in coins:
            if cost - coin >= 0:
                num_coins = min( num_coins, 1 + find_min_num_coins(cost - coin) )
            else:
                min_greater_cost = min(min_greater_cost, abs(cost - coin))

        if num_coins == float('inf'):   # se non trovo alcuna soluzione con il costo assegnato
            num_coins = find_min_num_coins(cost + min_greater_cost) # tento con un valore maggiore

        memo[cost] = num_coins
        return num_coins
    
    return find_min_num_coins(V)

def test_func(value, coins, result): # funzione per il testing
    num_coins = find_coins(value, coins)
    if num_coins == result:
        return True, num_coins
    else:
        return False, num_coins  

if __name__ == '__main__':

    array_test0 = [10, 2, 1, 5]
    array_test1 = [7, 4, 1, 3, 4, 5]
    array_test2 = [13, 2, 5]
    array_test3 = [10, ]
    array_test4 = [0, 10]

    print('\n')

    print('[TEST CASE 0] Testing array [value - coins]: ' + str(array_test0[0]) + ' - ' + str(array_test0[1:]))
    success, num_coins = test_func(array_test0[0], array_test0[1:], 2)
    if success:
        print('Result: ' + str(num_coins) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(num_coins) + ' -> FAILURE.')

    print('\n[TEST CASE 1] Testing array [value - coins]: ' + str(array_test1[0]) + ' - ' + str(array_test1[1:]))
    success, num_coins = test_func(array_test1[0], array_test1[1:], 2)
    if success:
        print('Result: ' + str(num_coins) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(num_coins) + ' -> FAILURE.')

    print('\n[TEST CASE 2] Testing array [value - coins]: ' + str(array_test2[0]) + ' - ' + str(array_test2[1:]))
    success, num_coins = test_func(array_test2[0], array_test2[1:], 4)
    if success:
        print('Result: ' + str(num_coins) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(num_coins) + ' -> FAILURE.')

    print('\n[TEST CASE 3] Testing array [value - coins]: ' + str(array_test3[0]) + ' - ' + str(array_test3[1:]))
    success, num_coins = test_func(array_test3[0], array_test3[1:], -1)
    if success:
        print('Result: ' + str(num_coins) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(num_coins) + ' -> FAILURE.')

    print('\n[TEST CASE 4] Testing array [value - coins]: ' + str(array_test4[0]) + ' - ' + str(array_test4[1:]))
    success, num_coins = test_func(array_test4[0], array_test4[1:], 0)
    if success:
        print('Result: ' + str(num_coins) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(num_coins) + ' -> FAILURE.')

    print('\n')    
