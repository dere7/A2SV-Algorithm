class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        start = max_len = 0
        for end, c in enumerate(s):
            while c in chars:
                chars.remove(s[start])
                start += 1
            chars.add(c)
            max_len = max(max_len, end - start + 1)
        return max_len