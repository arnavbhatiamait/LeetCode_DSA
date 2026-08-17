class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs={}
        ft={}
        if len(s)!=len(t):
            return False
        for i in s:
            fs[i]=fs.get(i,0)+1
        for i in t:
            ft[i]=ft.get(i,0)+1

        for i in fs.keys():
            if fs[i] != ft.get(i, 0):
                return False
        return True