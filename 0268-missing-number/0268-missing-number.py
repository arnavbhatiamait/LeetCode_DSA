class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        remaining_sum=(n)*(n+1)/2
        for i in nums:
            remaining_sum-=i
        return int(remaining_sum)