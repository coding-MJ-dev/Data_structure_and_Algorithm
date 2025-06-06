#217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        
# Time Complexity: O(n)
# Space Complexity: O(n)
# The first solution uses a set to check for duplicates, which is efficient.
# The second solution sorts the list first, which has a time complexity of O(n log n).
# Both solutions have a space complexity of O(n) due to the use of a set or the sorted list.
# The first solution is more efficient in terms of time complexity.
# The second solution is less efficient due to the sorting step.
# The first solution is preferred for its simplicity and efficiency.