# 68. Text Justification


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur = []
        curlen = 0
        for w in words:
            if len(cur) + curlen + len(w) > maxWidth:
                blank = maxWidth - curlen
                add = max(len(cur) - 1, 1)
                while blank > 0:
                    for i in range(add):
                        if blank == 0:
                            break
                        cur[i] += " "
                        blank -= 1
                s = "".join(cur)
                # print(cur)
                ans.append(s)
                cur = []
                curlen = 0
            curlen += len(w)
            cur.append(w)
        blank = maxWidth - curlen
        s = " ".join(cur) + " " * (blank - max(0, len(cur) - 1))
        ans.append(s)
        return ans
