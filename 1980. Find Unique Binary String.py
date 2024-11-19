# 1980. Find Unique Binary String

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        check = nums[0]
        nums = set(nums)
        
        cur = ""
        for i in range(len(nums)):
            if check[i] == "0":
                if check[:i] + "1" + check[i+1:] not in nums:
                    return check[:i] + "1" + check[i+1:]
            else:
                if check[:i] + "0" + check[i+1:] not in nums:
                    return check[:i] + "0" + check[i+1:]