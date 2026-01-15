class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_water = 0
        #Note: Area = height x Width
        while l<r:
            w = r-l
            h = min(height[l], height[r])
            current_area = h * w
            
            max_water = max(current_area, max_water)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_water
            