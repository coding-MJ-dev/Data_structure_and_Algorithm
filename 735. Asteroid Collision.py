# 735. Asteroid Collision


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if not stack:
                stack.append(n)
            elif stack[-1] < 0:
                stack.append(n)
            elif stack[-1] > 0 and n > 0:
                stack.append(n)
            else:
                while stack and stack[-1] > 0 and stack[-1] + n < 0:
                    stack.pop()
                if stack and stack[-1] + n == 0:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(n)

        return stack
