class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        remaining_sum=((n)*(n+1))//2
        for i in range(n):
            remaining_sum-=nums[i]
        return remaining_sum