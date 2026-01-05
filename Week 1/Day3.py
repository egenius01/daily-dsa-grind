class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notebook = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in notebook:
                return [notebook[difference], i]
            notebook[n] = i


        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     if difference in notebook:
        #         return [notebook[difference], i]
        #     notebook[nums[i]] = i