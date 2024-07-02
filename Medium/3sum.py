# Problem 15 - 3Sum
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sums = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if v + nums[l] + nums[r] == 0:
                    sums.append([v, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif v + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return sums