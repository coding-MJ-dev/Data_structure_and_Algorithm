# 926. Flip String to Monotone Increasing
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
            else:
                ans = min(ones, ans + 1)
        return ans


# 
        # left_ones = 0
        # right_zeros = s.count("0")
        # ans = right_zeros
        # for c in s:
        #     if c == "0":
        #         right_zeros -= 1
        #     else:
        #         left_ones += 1
        #     ans = min(ans, left_ones + right_zeros)
        
        # return ans