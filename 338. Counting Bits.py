class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        pivot = 1
        ans = [0] * (n + 1)
        ans[1] = 1
        i = 2
        while i < n + 1:
            if i / 2 == pivot:
                pivot = i
            ans[i] = 1 + ans[i - pivot]
            i += 1

        return ans


sol = Solution()
print(sol.countBits(5))
