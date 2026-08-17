class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        m=(l+h)//2
        ans=m
        while(l<=h):
            if target==nums[m]:
                return m
            elif target>nums[m]:
                l=m+1
            else:
                h=m-1
            m=(l+h)//2
            ans=l
        return ans