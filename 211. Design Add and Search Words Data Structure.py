# 211. Design Add and Search Words Data Structure


class trieNode:
    def __init__(self):
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = trieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = trieNode()
            cur = cur.children[c]
        cur.children["&"] = []

    def search(self, word: str) -> bool:
        cur = self.root
        res = False

        def dfs(i, cur):
            nonlocal res
            if i == len(word):
                if "&" in cur.children:
                    res = True
                return

            if word[i] != ".":
                if word[i] in cur.children:
                    cur = cur.children[word[i]]
                    dfs(i + 1, cur)

            elif word[i] == ".":
                for c in cur.children:
                    if c == "&":
                        continue
                    dfs(i + 1, cur.children[c])

            else:
                return
            # return True

        dfs(0, cur)
        return res
