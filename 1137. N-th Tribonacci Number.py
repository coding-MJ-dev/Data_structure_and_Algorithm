# 1137. N-th Tribonacci Number


class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {}
        dic[0] = 0
        dic[1] = 1
        dic[2] = 1

        if n <= 2:
            return dic[n]

        i = 3
        while i < n + 1:
            dic[i] = dic[i - 1] + dic[i - 2] + dic[i - 3]
            i += 1

        return dic[n]
