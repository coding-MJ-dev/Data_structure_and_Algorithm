# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans <<= 1
            ans += n & 1
            n >>= 1

        return ans
    
    
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             digit = n >> i & 1
#             res = digit << (31 - i) | res

#         return res
