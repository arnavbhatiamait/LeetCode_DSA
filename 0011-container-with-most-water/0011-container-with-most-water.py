class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_cap=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            max_cap=max(max_cap,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_cap
