from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mail_map = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            mail_map[sorted_word].append(word)
        return list(mail_map.values())