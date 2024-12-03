## 2459. Sort Array by Moving Items to Empty Space

class Solution:
    def sortArray(self, nums: List[int]) -> int:
        # O(n) O(n)
        n = len(nums)

        def solve(nums):
            res = 0
            for i in range(n):
                # moving first element that is in wrong position to pos '0'
                if i > 0 and nums[i] != i:
                    nums[0] = nums[i]
                    nums[i] = 0
                    res += 1
                # swap element at pos '0' until all elements are in their place
                while nums[0] != 0:
                    pos = nums[0]
                    nums[0], nums[pos] = nums[pos], nums[0]
                    res += 1
            return res
        
        # copy + shift elements one position right
        nums2 = [nums[-1]] + nums[:-1]
        
        return min(solve(nums), solve(nums2))




        
                                                                                            
        # n = len(nums)
        # pos = [0]*n
        # for i, k in enumerate(nums): pos[k] = i      # [1] enumerate positions of elements in 'nums'
        
        # def permute(pos, s):                         # [2] this function realises a minimal permutation 
        #     cnt, nxt = 0, 1                          #     scheme for both 0-indexed and 1-indexed arrays 
            
        #     while nxt < n:
        #         if pos[0] == s * (n-1):              # [3] if '0' was found in one of terminal positions 
        #             while pos[nxt] == nxt-s:         #     (0 or n-1) then we have to swap '0' with the 
        #                 nxt += 1                     #     first incorrectly placed number
        #                 if nxt == n: return cnt      # [4] or return if all numbers are now in order 
        #             ni = nxt
        #         else: ni = pos[0] + s                # [5] '0' was found in a regular (non-terminal) position
                
        #         pos[0], pos[ni] = pos[ni], pos[0]    # [6] here, the swap happens
        #         cnt += 1   
                
        # return min(permute(list(pos), 0),            # [7] try permuting using both indexing schemes, 
        #            permute(list(pos), 1))            #     then choose the minimal result




# Hard # Topics # Companies # Hint
# You are given an integer array nums of size n containing each element from 0 to n - 1 (inclusive). Each of the elements from 1 to n - 1 represents an item, and the element 0 represents an empty space.

# In one operation, you can move any item to the empty space. nums is considered to be sorted if the numbers of all the items are in ascending order and the empty space is either at the beginning or at the end of the array.

# For example, if n = 4, nums is sorted if:

# nums = [0,1,2,3] or
# nums = [1,2,3,0]
# ...and considered to be unsorted otherwise.

# Return the minimum number of operations needed to sort nums.

 

# Example 1:

# Input: nums = [4,2,0,3,1]
# Output: 3
# Explanation:
# - Move item 2 to the empty space. Now, nums = [4,0,2,3,1].
# - Move item 1 to the empty space. Now, nums = [4,1,2,3,0].
# - Move item 4 to the empty space. Now, nums = [0,1,2,3,4].
# It can be proven that 3 is the minimum number of operations needed.
# Example 2:

# Input: nums = [1,2,3,4,0]
# Output: 0
# Explanation: nums is already sorted so return 0.
# Example 3:

# Input: nums = [1,0,2,4,3]
# Output: 2
# Explanation:
# - Move item 2 to the empty space. Now, nums = [1,2,0,4,3].
# - Move item 3 to the empty space. Now, nums = [1,2,3,4,0].
# It can be proven that 2 is the minimum number of operations needed.
 

# Constraints:

# n == nums.length
# 2 <= n <= 105
# 0 <= nums[i] < n
# All the values of nums are unique.








# 