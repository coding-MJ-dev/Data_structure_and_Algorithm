# 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uni = set(nums1) & set(nums2)
        
        return [list(set(nums1) - uni), list(set(nums2) - uni)]
