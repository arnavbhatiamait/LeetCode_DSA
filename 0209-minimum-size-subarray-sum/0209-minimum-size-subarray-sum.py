import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=sys.maxsize
        l=0
        r=0
        sums=0
        while(r<len(nums)):
            
            sums+=nums[r]
            while sums>=target:
                min_len=min(min_len,r-l+1)
                sums-=nums[l]
                l+=1
            r+=1
        

        if min_len==sys.maxsize:
            return 0
        return min_len
