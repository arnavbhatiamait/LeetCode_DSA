class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        k_v={}
        for i in nums:
            k_v[i]=k_v.get(i,0)+1
        sorted_items = sorted(k_v.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans