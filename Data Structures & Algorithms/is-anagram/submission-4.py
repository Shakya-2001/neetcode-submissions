class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        aka = {}
        for i in s:
            aka[i]=aka.get(i,0)+1
        
        for i in t:
            if i not in aka:
                return False
            aka[i]-=1
        
            if aka[i]<0:
                return False
        return True
        