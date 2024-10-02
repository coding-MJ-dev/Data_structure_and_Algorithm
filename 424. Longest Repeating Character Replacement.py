# 424. Longest Repeating Character Replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curMax = 0
        dic = defaultdict(int)
        i = 0
        ans = 1
        for j, c in enumerate(s):
            dic[c] += 1
            curMax = max(dic[c], curMax)
            if (j - i + 1) - curMax <= k:
                ans = max(ans, j - i + 1)
            else:
                dic[s[i]] -= 1
                i += 1
        return ans
