# Problem 11 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1

        while l < r:
            mul = min(height[l], height[r]) * (r - l)
            res = max(res, mul)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        
        return res