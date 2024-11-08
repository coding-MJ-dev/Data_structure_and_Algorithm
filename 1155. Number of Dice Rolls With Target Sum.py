#  1155. Number of Dice Rolls With Target Sum



class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 내가 그냥 한 번에 해냄 짱
        mod = (10**9) + 7
        dp = {i+1 : 1 for i in range(k)}

        for i in range(n-1):
            newdp = defaultdict(int)
            for j in range(1,k+1):
                for d in dp:
                    if j + d <= target:
                        newdp[j+d] += dp[d]
            dp = newdp
                        


        # print(dp)
        return dp[target] % mod if target in dp else 0