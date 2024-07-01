# Problem 347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        top = {}

        for num in nums:
            if num in top:
                top[num] += 1
            else:
                top[num] = 1

            

        return [item[0] for item in (sorted(top.items(), key=lambda item: item[1])[-k:])]