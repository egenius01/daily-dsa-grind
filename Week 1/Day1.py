"""

Day1 - Problem-217 Contains Duplicate

"""
class Solution:


    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Method 1
        '''    
        # nums_lenght = len(nums)
        # nums_set_lenght = len(set(nums))
        # if nums_lenght == nums_set_lenght:
        #     return False
        # return True

        '''
                Method 2
        '''        

        return len(nums) != len(set(nums)) 
        #Most Efficient due to using in built python function which uses C an has very minimal interpreter overhead (4ms | 28.92mb); 
        #Big (O) Notation: O(n)

        '''
                Method 3
        '''    

        # notebook = set()
        # for i in nums:
        #     if i in notebook:
        #         return True
        #     notebook.add(i)
        # return False