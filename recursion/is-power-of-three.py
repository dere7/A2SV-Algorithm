import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if math.fabs(n) < 1:
            return False
        return self.isPowerOfThree(n / 3) # type: ignore