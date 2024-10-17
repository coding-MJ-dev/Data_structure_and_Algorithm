# 605. Can Place Flowers


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True

        while i < len(flowerbed):
            if (
                flowerbed[i] == 0
                and flowerbed[max(0, i - 1)] != 1
                and flowerbed[min(len(flowerbed) - 1, i + 1)] != 1
            ):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                # print(flowerbed)
                return True
            i += 1
        return False
