class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==1 or k==0:
            return 0
        cur_prod=1
        l=0
        ans=0
        r=0
        while (r<len(nums)):
            cur_prod*=nums[r]
            while cur_prod>=k:
                cur_prod//=nums[l]
                l+=1
            ans+=r-l+1
            r+=1
        return ans
