def coinChange(n, coins, results):

    min_coins = n
    if n in coins:
        results[n] = 1
        return 1

    elif results[n] > 0:
        return results[n]

    else:
        for i in [x for x in coins if x <= n]:
            num_coins = 1+coinChange(n-i, coins, results)

            if num_coins < min_coins:
                min_coins = num_coins
                results[n] = min_coins

    return min_coins


print coinChange(74,[1,5,10,25],[0]*75)