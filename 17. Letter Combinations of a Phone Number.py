# 17. Letter Combinations of a Phone Number


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []
        if not digits:
            return []

        def dfs(i, cur):
            if len(cur) >= len(digits):
                ans.append(cur[:])
                return
            if i >= len(digits):
                return

            for c in dic[digits[i]]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[:-1]

        dfs(0, "")
        return ans
