# Problem 1 - Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}

        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i