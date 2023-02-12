from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        maxSum = 0
        n = len(nums)
        for i in range(n - firstLen + 1):
            max1 = sum(nums[i:i + firstLen])
            if secondLen <= i:
                for j in range(i - secondLen + 1):
                    max2 = sum(nums[j:j + secondLen])
                    maxSum = max(maxSum, max1 + max2)

            if len(nums) - (i + 1) >= secondLen:
                j = 0
                while j + i + secondLen <= len(nums):
                    max2 = sum(nums[i + j + firstLen:i + j + firstLen + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1
        return maxSum