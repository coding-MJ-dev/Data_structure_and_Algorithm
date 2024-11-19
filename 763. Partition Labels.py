# 763. Partition Labels


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = i
        
        ans = []
        start = 0
        last = 0
        for i, c in enumerate(s):
            last = max(last, seen[c])
            if i == last:
                ans.append(i - start + 1)
                start = i+1
        return ans 