coins = [1,2,5]
target = 5

dp = [[0 for _ in range(target+1)]for _ in range(len(coins)+1)]

for i in range(len(coins)+1):
    for j in range(target+1):
        if i==0 and j ==0:
            dp[i][j] = 0
        elif j==0:
            dp[i][j] = 1
        elif coins[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        
print('Total Number of ways to make target: ',dp[len(coins)][target])

print("Show the table: ")

for i in range(len(coins)+1):
    for j in range(target+1):
        print(dp[i][j],end = ' ')
    print()
        
        
        