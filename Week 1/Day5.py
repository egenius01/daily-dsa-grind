from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums)+1)]
        count_map = Counter(nums)
        for n,c in count_map.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1,0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res