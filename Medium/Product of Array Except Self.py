# Problem 238 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = 0
        mul = 1

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                mul *= num
        
        
        if zeros >= 2:
            return [0] * len(nums)
        elif zeros == 1:
            answer = [0] * len(nums)

            zero_index = nums.index(0)
            answer[zero_index] = mul
        else:
            answer = [mul] * len(nums)
            for i in range(len(nums)):
                answer[i] = int(answer[i]/nums[i])
        
        return answer