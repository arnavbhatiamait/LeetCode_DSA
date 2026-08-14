class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum =0
        for j in range(len(accounts)):
            temp_sum=0
            for i in range(len(accounts[j])):
                temp_sum+=accounts[j][i]
            if max_sum<temp_sum:
                max_sum=temp_sum
        return max_sum