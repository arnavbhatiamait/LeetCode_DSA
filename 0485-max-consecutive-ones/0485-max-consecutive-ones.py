class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons=0
        current_cons=0
        for i in range(len(nums)):
            if nums[i]!=1:
                current_cons=0
            elif nums[i]==1:
                current_cons+=1
            max_cons=max(max_cons,current_cons)
        return max_cons
