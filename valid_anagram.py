class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = {}
        m = {}
        for i in range(0,len(s)):
            if s[i] in n:
                n[s[i]] += 1
            else:
                n[s[i]] = 1
        
        for i in range(0,len(t)):
            if t[i] in m:
                m[t[i]] += 1
            else:
                m[t[i]] = 1
        
        if n == m:
            return True
        else:
            return False