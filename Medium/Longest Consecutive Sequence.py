# Problem 128 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        new_nums = set(nums)
        lcs = 0
        current = 1

        for num in new_nums:
            if num - 1 in new_nums:
                continue
            else:
                while num + 1 in new_nums:
                    num += 1
                    current +=1
                if current > lcs: lcs = current
                current = 1

        return lcs