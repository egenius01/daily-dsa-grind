class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False
        # s_comp = {}
        # t_comp = {}
        
        # for i in range(len(s)):
        #     s_comp[s[i]] = s_comp.get(s[i], 0) + 1
        #     t_comp[t[i]] = t_comp.get(t[i], 0) + 1
        
        # return s_comp == t_comp