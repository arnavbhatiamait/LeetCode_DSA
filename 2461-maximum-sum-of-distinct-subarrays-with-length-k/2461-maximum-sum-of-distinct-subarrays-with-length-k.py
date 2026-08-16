class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        cur_sum=0
        ans=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            freq[nums[i]]=freq.get(nums[i],0)+1
            if i>=k:
                cur_sum-=nums[i-k]
                freq[nums[i-k]]-=1
                if freq[nums[i-k]]==0:
                    del(freq[nums[i-k]])
            if i>=k-1 and len(freq)==k:
                ans=max(ans,cur_sum)
        return ans