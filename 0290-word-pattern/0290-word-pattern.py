class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False
        p_s={}
        s_p={}
        ls=s.split(" ")
        
        for i in range(len(pattern)):
            a=pattern[i]
            b=ls[i]
            if a in p_s and p_s[a]!=b:
                return False
            if b in s_p and s_p[b]!=a:
                return False
            s_p[b]=a
            p_s[a]=b
        return True