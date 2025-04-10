# 312. Burst Balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in range(n-2, 0, -1): # 터뜨릴 수 있는 가장  왼쪽거
            for right in range(left, n-1): # 터트릴 가장 오른쪽거
                for i in range(left, right + 1): # 그거를 왼쪽부터 터뜨려보자
                    last_pop =  nums[left-1] * nums[i] * nums[right+1]
                    remain = dp[left][i-1] + dp[i+1][right] # 방금 계산 한거 + 아까 계산한 아랫줄(이 풍선 없는 조합)
                    dp[left][right] = max(dp[left][right], last_pop + remain)
            
        return dp[1][n-2]