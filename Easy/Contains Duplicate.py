# Problem 217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
