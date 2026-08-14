class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs=0
        ans_list=[]
        for i in nums:
            rs+=i
            ans_list.append(rs)
        return ans_list
        