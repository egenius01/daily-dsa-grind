from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if n-1 not in numset:
                length = 0

                #now we set the while loop to as long as n+1 is in the numset
                while n+(length) in numset:
                    length+=1
                
                #now we check the maximum value between the current length and the current longest values.
                longest = max(longest, length)
        return longest