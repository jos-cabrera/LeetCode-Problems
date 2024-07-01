# Problem 167 - Two Sum II Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1
        return [l+1, r+1]