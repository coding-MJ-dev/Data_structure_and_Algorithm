# 1921. Eliminate Maximum Number of Monsters


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [x / y for x, y in zip(dist, speed)]
        time.sort()

        for i in range(1, len(time)):

            if time[i] <= i:
                return i
        return len(time)
        


        # arrive = [(d/s) for d, s in zip(dist, speed)]
        # arrive.sort()
        # ans = 0

        # for i in range(len(arrive)):
        #     if arrive[i] <= i:
        #         break
        #     ans += 1

        # return ans
