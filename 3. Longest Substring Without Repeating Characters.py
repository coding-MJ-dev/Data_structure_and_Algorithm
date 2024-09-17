# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        ans = 0
        for j, c in enumerate(s):
            if c not in seen:
                ans = max(j - i + 1, ans)
            else:
                while i < j and s[i] != c:
                    del seen[s[i]]
                    i += 1
                i += 1
            seen[c] = j
        return ans
