from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j , k = i + 1, n - 1
            while j < k:
                triples = [nums[i], nums[j], nums[k]]
                sum_triples = sum(triples)
                if sum_triples == 0:
                    result.append(triples)
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif sum_triples < 0:
                    j += 1
                else:
                    k -= 1

        return result   