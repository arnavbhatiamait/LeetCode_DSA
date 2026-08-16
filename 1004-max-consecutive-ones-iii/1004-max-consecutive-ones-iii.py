class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        rem_flip=k
        max_len=0
        while(r<len(nums)):
            if nums[r]==1:
                r+=1
            elif nums[r]==0 and rem_flip>0:
                rem_flip-=1
                r+=1
            else:
                if nums[l]==0:
                    rem_flip+=1
                l+=1
            max_len=max(max_len,r-l)
        return max_len
        