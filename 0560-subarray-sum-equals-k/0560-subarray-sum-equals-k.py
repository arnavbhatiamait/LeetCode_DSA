class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        freq[0] = 1
        ans = 0
        sums = 0
        for i in nums:
            sums += i
            rem = sums - k
            if rem in freq:
                ans += freq[rem]
            freq[sums] = freq.get(sums, 0) + 1
        print(freq)
        return ans