# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        ans = 0
        i = 0
        curSum = 0
        for j, n in enumerate(arr):
            curSum += n
            if j - i + 1 == k:
                if curSum // k >= threshold:
                    ans += 1
                curSum -= arr[i]
                i += 1
        return ans
