# 946. Validate Stack Sequences


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while i < len(pushed):
            stack.append(pushed[i])
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            i += 1

        while stack and popped[j] == stack[-1]:
            stack.pop()
            j += 1

        return True if len(stack) == 0 else False
