# 150. Evaluate Reverse Polish Notation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 다시 풀어 #내가 해냄 #하지만 더 잘할 수 있음
        stack = []
        i = 0
        ans = 0
        while i < len(tokens):
            if tokens[i] not in ("+", "-", "*", "/"):
                n = int(tokens[i])
                stack.append(n)
            else:
                # print(stack)
                d2 = stack.pop()
                d1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(d1 + d2)
                elif tokens[i] == "-":
                    stack.append(d1 - d2)
                elif tokens[i] == "*":
                    stack.append(d1 * d2)
                else:
                    n = int(d1 / d2)
                    stack.append(n)

            i += 1

        return stack[0]
