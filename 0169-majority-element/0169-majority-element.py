class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value_dict={}
        for i in nums:
            value_dict[i]=value_dict.get(i,0)+1
        for k in value_dict.keys():
            if value_dict[k]>len(nums)//2:
                return k
