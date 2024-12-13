def find_coins(V: int, coins: list[int]) -> int:

    n = len(coins)
    if n == 0 or V < 0:
        return -1
        
    memo = {}
    
    def find_min_num_coins(cost):
        
        if cost == 0:
            return 0 
        
        if cost in memo:
            return memo[cost]
        
        num_coins = float('inf')
        for coin in coins:
            if cost - coin >= 0:
                num_coins = min( num_coins, 1 + find_min_num_coins(cost - coin) )

        memo[cost] = num_coins
        return num_coins
    
    num_coins = find_min_num_coins(V)
    return -1 if num_coins == float('inf') else num_coins
