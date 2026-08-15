class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l_max = [0] * n
        r_max = [0] * n
        l_max[0]=height[0]
        ans=0
        r_max[len(height)-1]=height[len(height)-1]
        # ! left max val
        for i in range(1,len(height)):
            l_max[i]=max(l_max[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            r_max[i]=max(r_max[i+1],height[i])
        for i in range(len(height)):
            ans+=min(l_max[i],r_max[i])-height[i]
        return ans