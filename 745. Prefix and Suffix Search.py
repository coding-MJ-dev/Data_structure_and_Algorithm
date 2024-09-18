# 745. Prefix and Suffix Search
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class WordFilter:

    def __init__(self, words: List[str]):
        self.wordlist = []
        self.wordDic = defaultdict(list)

        self.pref_root = TrieNode()
        self.suf_root = TrieNode()
        for word in words:
            if word not in self.wordDic:
                # make trie
                cur = self.pref_root
                cur2 = self.suf_root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    # cur.words.append(word)
                    cur = cur.children[c]
                    cur.words.append(word)
                # cur.words.append(word)

                for c in reversed(word):
                    if c not in cur2.children:
                        cur2.children[c] = TrieNode()

                    cur2 = cur2.children[c]
                    cur2.words.append(word)
                # cur2.words.append(word)

            i = len(self.wordlist)
            self.wordlist.append(word)
            self.wordDic[word].append(i)

            print()

    def f(self, pref: str, suff: str) -> int:
        cur1 = self.pref_root
        cur2 = self.suf_root
        for c in pref:
            if c not in cur1.children:
                return -1
            cur1 = cur1.children[c]
        pref_set = set(cur1.words)

        for c in reversed(suff):
            if c not in cur2.children:
                return -1
            cur2 = cur2.children[c]
        suff_set = set(cur2.words)
        ans_set = pref_set & suff_set
        ans = -1
        for w in ans_set:
            ans = max(ans, self.wordDic[w][-1])
        return ans
