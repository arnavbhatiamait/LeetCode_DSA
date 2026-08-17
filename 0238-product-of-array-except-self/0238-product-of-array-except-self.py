class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods=1
        zero_count=nums.count(0)
        if zero_count>=2:
            return [0]*len(nums)
        for i in nums:
            if i==0:
                continue
            prods*=i
        # ans=[]
        for i in range(len(nums)):
            if zero_count==1:
                if nums[i]==0:
                    nums[i]=prods
                else:
                    nums[i]=0
            else:
                nums[i]=prods//nums[i]

        return nums