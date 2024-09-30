target = 8
coins = [1,3,5]
len_of_coins = len(coins)

dp = [[0 for _ in range(target + 1)] for _ in range(len_of_coins + 1)]

for i in range(0,len_of_coins+1):
    for j in range(0,target + 1):
        if i ==0 and j ==0:
            dp[i][j] = 1
        elif i == 0:
            dp[i][j] = 0
        elif coins[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
print(dp[len_of_coins][target])


for i in range(0, len_of_coins + 1):
    for j in range(0, target + 1):
        print(dp[i][j], end=' ')   
    print()   