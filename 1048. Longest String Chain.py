# 1048. Longest String Chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 1
        dp = {}
        for word in sorted(words, key=len):
            if word in dp:
                continue
            dp[word] = 1
            for i in range(len(word)):
                cur = word[:i] + word[i+1:]
                if cur in dp:
                    dp[word] = max(dp[word], dp[cur]+1)
            ans = max(ans, dp[word])
        return ans
