from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_fruits = start = 0
        table = {}
        for end in range(n):
            if fruits[end] in table.keys():
                table[fruits[end]] += 1
            else:
                table[fruits[end]] = 1
            while len(table) > 2:
                table[fruits[start]] -= 1
                if table[fruits[start]] == 0:
                    del table[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
        return max_fruits