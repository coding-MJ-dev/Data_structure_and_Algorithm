# 935. Knight Dialer


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        jump = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        mod = 10**9 + 7
        dp = [1] * 10
        count = 1
        while count < n:
            newdp = [0] * 10
            for i in range(10):
                for num in jump[i]:
                    newdp[num] += dp[i] % mod
            dp = newdp
            count += 1

        return sum(dp) % mod
