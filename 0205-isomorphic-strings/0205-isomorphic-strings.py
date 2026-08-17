class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_t={}
        t_s={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]
            if a in s_t and s_t[a]!=b:
                return False
            if b in t_s and t_s[b]!=a:
                return False
            s_t[a]=b
            t_s[b]=a
        return True 
