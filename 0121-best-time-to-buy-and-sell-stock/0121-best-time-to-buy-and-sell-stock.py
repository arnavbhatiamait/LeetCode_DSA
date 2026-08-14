class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        chepest=prices[0]
        max_prof=0
        for i in prices[1:]:
            chepest=min(i,chepest)
            max_prof=max(max_prof,i-chepest)
        return max_prof