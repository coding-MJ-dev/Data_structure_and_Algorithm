# 76. Minimum Window Substring


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = collections.Counter(t)
        need = len(t)
        ansLen = len(s)
        i, I, J = 0, None, None
        for j, n in enumerate(s):
            if n in count:
                if count[n] > 0:
                    need -= 1
                    count[n] -= 1
                    if need == 0:

                        if I == None or j - i + 1 < ansLen:
                            I = i
                            J = j
                            ansLen = min(j - i + 1, ansLen)
                        while need == 0:
                            if s[i] in count:
                                count[s[i]] += 1

                            if j - i + 1 < ansLen:
                                I = i
                                J = j
                                ansLen = min(j - i + 1, ansLen)

                            if count[s[i]] == 1:
                                need += 1
                            i += 1

                else:
                    count[n] -= 1
        return s[I : J + 1] if I != None and J != None else ""
