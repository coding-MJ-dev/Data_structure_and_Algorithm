# 395. Longest Substring with At Least K Repeating Characters



class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = collections.Counter(s)
        count = list(count.items())
        count.sort(key = lambda x: x[1])
        if count[0][1] >= k:
            return len(s)

        return max(self.longestSubstring(t, k) for t in s.split(count[0][0]))








        # count = Counter(s)
        # bad = set()
        # for c in count:
        #     if count[c] < k:
        #         bad.add(c)
        # if not bad: return len(s)

        # substrings = []
        # cur = ""
        # for c in s:
        #     if c in bad:
        #         if cur:
        #             substrings.append(cur)
        #             cur = ""
        #     else:
        #         cur += c
        # if cur: substrings.append(cur)
        # results = [self.longestSubstring(sub, k) for sub in substrings]
        # if not results: return 0
        # return max(results)


        # if not s:
        #     return 0
        # c = min(set(s), key = s.count)
        # if s.count(c) >= k:
        #     return len(s)
        # return max(self.longestSubstring(t, k)  for t in s.split(c))




















        # if len(s) < k:
        #     return 0
        # c = min(set(s), key=s.count)
        # if s.count(c) >= k:
        #     return len(s)
        # return max(self.longestSubstring(t, k) for t in s.split(c))

