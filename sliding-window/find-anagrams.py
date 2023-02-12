from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_chars = {}
        p_chars = {}
        ns, np = len(s), len(p)
        answer = []
        if np > ns:
            return []
        for i in range(np):
            s_chars[s[i]] = s_chars.get(s[i], 0) + 1
            p_chars[p[i]] = p_chars.get(p[i], 0) + 1
        if s_chars == p_chars:
            answer.append(0)
        start = 0
        for end in range(np, ns):
            s_chars[s[end]] = s_chars.get(s[end], 0) + 1
            s_chars[s[start]] -= 1

            if s_chars[s[start]] == 0:
                del s_chars[s[start]]

            start += 1
            if s_chars == p_chars:
                answer.append(start)
        return answer