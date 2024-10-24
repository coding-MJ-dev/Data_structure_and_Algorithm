# 239. Sliding Window Maximum


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        ans = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                stack.pop()
            stack.append(i)

            if i >= k - 1:
                while stack and stack[0] <= i - k:
                    stack.popleft()
                ans.append(nums[stack[0]])

        return ans
