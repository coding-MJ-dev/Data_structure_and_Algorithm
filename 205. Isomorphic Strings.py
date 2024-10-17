# 205. Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        ans1, ans2 = [], []
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = i
            ans1.append(dic1[s[i]])
            if t[i] not in dic2:
                dic2[t[i]] = i
            ans2.append(dic2[t[i]])
        # print(dic1, dic2)
        # print(ans1, ans2)
        return ans1 == ans2
