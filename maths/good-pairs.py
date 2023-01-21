from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        goodPairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    goodPairs += 1
        return goodPairs