# Problem 42 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, len(height) - 1

        while height[l] < height[l+1] and l < len(height) - 2:
            l += 1

        while height[r] < height[r-1]:
            r -= 1

        if r - l < 2:
            return 0

        vl, vr = height[l], height[r]
        res = 0

        while l < r:

            while vl <= vr and l < r:
                l += 1
                diffl = vl - height[l]

                if diffl < 0:
                    vl = height[l]
                else:
                    res += diffl
                
            while vr <= vl and l < r:
                r -= 1
                diffr = vr - height[r]
                
                if diffr < 0:
                    vr = height[r]
                else:
                    res += diffr
    
        return res