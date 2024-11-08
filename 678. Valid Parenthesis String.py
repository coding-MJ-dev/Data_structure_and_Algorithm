# 678. Valid Parenthesis String

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        special = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == "*":
                special.append(i)
            else:
                if stack:
                    stack.pop()
                elif special:
                    special.pop()
                else:
                    return False
            
        while stack:
            if not special or stack[-1] > special[-1]:
                return False
            stack.pop()
            special.pop()
        
        return True
