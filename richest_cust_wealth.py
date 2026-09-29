class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        for i in range(0,len(accounts)):
            sum = 0
            for j in range(0,len(accounts[i])):
                sum+=accounts[i][j]
            accounts[i] = sum
        return max(accounts)        