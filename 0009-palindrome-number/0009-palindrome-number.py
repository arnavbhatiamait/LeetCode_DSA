class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        num=0
        org=x
        while (x>0):
            rem=x%10
            num=num*10+rem
            x//=10
        print(num)
        return org==num 