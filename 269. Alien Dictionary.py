# 269. Alien Dictionary


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 가기 전에 읽어볼 것
        dic = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            wordlen = min(len(w1), len(w2))
            if len(w1) >= len(w2) and w1[:wordlen] == w2[:wordlen]:
                return ""
            for i in range(wordlen):
                if w1[i] != w2[i]:
                    dic[w1[i]].add(w2[i])
                    break

        ans = []
        visit = {}

        def dfs(c):  # is there any cycle
            if c in visit:
                return visit[c]
            if c not in visit:
                visit[c] = True
                for nei in dic[c]:
                    if dfs(nei):
                        return True
            visit[c] = False
            ans.append(c)
            return False

        for c in dic.keys():
            if dfs(c):
                return ""
        ans.reverse()
        return "".join(ans)
