class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        freq[0]=1
        prev_sum=0
        count=0
        for i in nums:
            prev_sum+=i
            target=prev_sum-k
            if target in freq:
                count+=freq[prev_sum-k]
            freq[prev_sum] = freq.get(prev_sum,0)+1
        return count
            

