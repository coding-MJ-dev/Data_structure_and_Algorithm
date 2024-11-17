# 1423. Maximum Points You Can Obtain from Cards


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cLen = len(cardPoints)
        if cLen == k:
            return sum(cardPoints)
        if cLen < k:
            return -1

        curSum = sum(cardPoints[-k:])
        ans = curSum
        for i in range(k):
            curSum += cardPoints[i] - cardPoints[i - k]
            ans = max(ans, curSum)
        
        return ans