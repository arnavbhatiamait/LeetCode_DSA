class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        m=(l+h)//2
        ans=0
        while l<=h:
            if m*m==x:
                return int(m)
            elif m*m>x:
                h=m-1
            else:
                ans=m
                l=m+1
            m=(l+h)//2
        return ans