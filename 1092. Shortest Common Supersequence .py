# 1092. Shortest Common Supersequence


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[""] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str1) - 1, -1, -1):
            for j in range(len(str2) - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    if len(dp[i][j + 1]) >= len(dp[i + 1][j]):
                        dp[i][j] = dp[i][j + 1]
                    else:
                        dp[i][j] = dp[i + 1][j]

        ans = ""
        str3 = dp[0][0]
        i, j, k = 0, 0, 0
        while i < len(str1) and j < len(str2) and k < len(str3):
            if str1[i] != str3[k]:
                ans += str1[i]
                i += 1
            elif str2[j] != str3[k]:
                ans += str2[j]
                j += 1
            else:
                ans += str3[k]
                k += 1
                i += 1
                j += 1

        return ans + str1[i:] + str2[j:]
