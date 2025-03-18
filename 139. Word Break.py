# 139. Word Break


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                wordlen = len(word)
                if i + wordlen <= len(s) and s[i: i+wordlen] == word:
                    dp[i] = max(dp[i+wordlen], dp[i])
        
        return True if dp[0] else False
            