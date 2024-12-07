# 1963. Minimum Number of Swaps to Make the String Balanced

class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0 # "["

        for c in s:
            if c == "[":
                count += 1
            else:
                if count > 0:
                    count -= 1
        return count // 2 if count % 2 == 0 else (count+1) // 2
