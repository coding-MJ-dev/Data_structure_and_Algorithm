# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = len(s1)
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        dic = defaultdict(int)
        for i in range(len(s2)):
            c = s2[i]
            dic[c] += 1
            if i >= l:
                dic[s2[i - l]] -= 1
                if dic[s2[i - l]] == 0:
                    del dic[s2[i - l]]
            # print(count, dic)
            if count == dic:
                return True

        return False
