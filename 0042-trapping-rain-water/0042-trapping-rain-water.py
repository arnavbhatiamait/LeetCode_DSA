class Solution:
    def trap(self, height: List[int]) -> int:
        # ! 2 pointer
        l_max=0
        r_max=0
        l=0
        n=len(height)
        r=n-1
        ans=0
        while(l<r):
            l_max=max(l_max,height[l])
            r_max=max(r_max,height[r])
            if l_max<r_max:
                ans+=l_max-height[l]
                l+=1
            else:
                ans+=r_max-height[r]
                r-=1
        return ans
