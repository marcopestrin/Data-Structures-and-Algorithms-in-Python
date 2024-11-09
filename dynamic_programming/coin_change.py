def change(coins, amount):
    dp = [0] * (amount + 1) # every element of this array rappresent a way to do the amount

    dp[0] = 1 
    
    for coin in coins:
        print(" ")
        print("-------> ",coin,":")
        for i in range(coin, amount + 1):
            print(i)
            dp[i] += dp[i - coin]
        print("--> dp:", dp)

    return dp[amount]


coins = [1, 2, 5]
amount = 8
result =change(coins, amount)
print(" ")
print("final result:",result)
