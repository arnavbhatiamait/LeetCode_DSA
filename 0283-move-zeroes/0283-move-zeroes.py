class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        i=0
        while(i<len(nums)):
            if nums[i]==0:
                nums.pop(i)
                k+=1
                continue
            i+=1
            
        nums.extend([0]*k)

        