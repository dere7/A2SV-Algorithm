from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        slow=fast=0
        while fast < n:
            chars[slow] = chars[fast]
            count = 1
            while fast + 1 < n and chars[fast] == chars[fast + 1]:
                fast += 1
                count += 1
            if count > 1:
                for c in str(count):
                    chars[slow + 1] = c
                    slow += 1
            fast += 1
            slow += 1
        return slow

chars = ["a","a","b","b","c","c","c"]
# chars = ["a","b","c"]
print(Solution().compress(chars))
print(chars)