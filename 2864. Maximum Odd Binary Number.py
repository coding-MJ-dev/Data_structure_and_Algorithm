# 2864. Maximum Odd Binary Number


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones

        return "0" * zeros + "1" if ones == 1 else "1" * (ones - 1) + "0" * zeros + "1"
