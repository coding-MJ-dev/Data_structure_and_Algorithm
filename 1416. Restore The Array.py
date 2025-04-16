# 1416. Restore The Array
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                continue
            for j in range(i, n):
                val = int(s[i:j+1])
                if val > k:
                    break
                else:
                    dp[i] += dp[j+1] % mod
        
        return dp[0] % mod

