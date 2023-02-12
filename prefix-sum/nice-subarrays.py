from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix  = odds = 0
        counter = { 0: 1 }
        for num in nums:
            if num % 2 != 0:
                prefix += 1
            odds += counter.get(prefix - k,0) 			
            counter[prefix] = counter.get(prefix, 0) + 1
        return odds