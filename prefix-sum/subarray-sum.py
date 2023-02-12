from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = cur_sum = count = 0
        prefixsum = {}        
        for i in nums:
            sum += i
            cur_sum = sum - k
            if sum == k:
                count += 1
            
            count += prefixsum.get(cur_sum, 0)
            prefixsum[sum] = 1 + prefixsum.get(sum, 0)
            
        return count