class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s="".join(s.split(" "))
        s = "".join(c for c in s if c not in string.punctuation)
        
        print(s)
        n=len(s)
        for i in range(n//2):
            if s[i]!=s[n-1-i]:
                return False
        return True