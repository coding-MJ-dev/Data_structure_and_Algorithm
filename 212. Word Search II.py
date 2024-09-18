# 212. Word Search II


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end = True
            cur.children["$"] = w

        def dfs(i, j, cur):
            if 0 <= i < rows and 0 <= j < cols and board[i][j] in cur.children:
                val = board[i][j]
                cur = cur.children[val]
                board[i][j] = "*"
                if cur.end == True:
                    if cur.children["$"] not in res:
                        res.append(cur.children["$"])

                dfs(i + 1, j, cur)
                dfs(i - 1, j, cur)
                dfs(i, j + 1, cur)
                dfs(i, j - 1, cur)
                board[i][j] = val

        res = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    cur = root
                    dfs(i, j, cur)

        return res

        # rows, cols = len(board), len(board[0])
        # ans = []

        # trie = {}
        # for w in words:
        #     cur = trie
        #     for c in w:
        #         if c not in cur:
        #             cur[c] = {}
        #         cur = cur[c]
        #     cur["@"] = w
        # print(trie)
        # def dfs(r, c, cur):
        #     val = board[r][c]
        #     cur = cur[val]

        #     if "@" in cur:
        #         print(cur)
        #         ans.append(cur["@"])
        #         del cur["@"]

        #     board[r][c] = "*"

        #     for dr, dc in ([-1,0], [1,0], [0,1], [0,-1]):
        #         new_r, new_c = r + dr, c + dc
        #         if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] in cur:
        #             dfs(new_r, new_c, cur)
        #     board[r][c] = val
        #     # print(board)

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] in trie:
        #             dfs(r, c, trie)

        # return ans
