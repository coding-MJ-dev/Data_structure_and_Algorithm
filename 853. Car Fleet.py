# 853. Car Fleet


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(x, y) for x, y in zip(position, speed)]
        pairs.sort(reverse=True)
        # print(pairs)
        stack = []
        for position, speed in pairs:
            time = (target - position) / speed
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)
