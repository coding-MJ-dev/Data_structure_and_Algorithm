# 605. Can Place Flowers


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Ind = {n: i for i, n in enumerate(nums1)}
        ans = [-1] * len(nums1)

        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                val = stack.pop()
                ind = nums1Ind[val]
                ans[ind] = n
            if n in nums1Ind:
                stack.append(n)

        return ans


# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         i = 0
#         if n == 0:
#             return True

#         while i < len(flowerbed):
#             if (
#                 flowerbed[i] == 0
#                 and flowerbed[max(0, i - 1)] != 1
#                 and flowerbed[min(len(flowerbed) - 1, i + 1)] != 1
#             ):
#                 flowerbed[i] = 1
#                 n -= 1
#             if n == 0:
#                 # print(flowerbed)
#                 return True
#             i += 1
#         return False
