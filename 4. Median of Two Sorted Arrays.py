# 4. Median of Two Sorted Arrays


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, k = 0, 0, 0
        prev, cur = 0, 0
        while k < (len(nums1) + len(nums2)) // 2 + 1:
            prev = cur
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    cur = nums1[i]
                    i += 1
                else:
                    cur = nums2[j]
                    j += 1
            elif i < len(nums1):
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
            k += 1

        if (len(nums1) + len(nums2)) % 2:
            return cur
        else:
            return (prev + cur) / 2
