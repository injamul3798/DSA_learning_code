coins = [1,2,5]
amount = 11
dp = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

for i in range(len(coins) + 1):
    for j in range(amount + 1):
        if i == 0 and j == 0:
            dp[i][j] = 0
        elif i == 0:
            dp[i][j] = float('inf')  
        elif j == 0:
            dp[i][j] = 0
        elif coins[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

# Return -1 if amount cannot be formed, else return the value
print(dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1)
