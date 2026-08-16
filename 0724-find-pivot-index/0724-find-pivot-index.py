class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t_sum=0
        for i in nums:
            t_sum+=i
        l_sum=0
        for i in range(len(nums)):
            r_sum=t_sum-l_sum-nums[i]
            if l_sum==r_sum:
                return i
            l_sum+=nums[i]
        return -1
