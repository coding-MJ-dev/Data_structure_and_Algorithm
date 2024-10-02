# 307. Range Sum Query - Mutable

# class NumArray:

#     def __init__(self, nums: List[int]):

#     def update(self, index: int, val: int) -> None:

#     def sumRange(self, left: int, right: int) -> int:


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


class segmentTree:
    def __init__(self, sum, L, R):
        self.sum = sum
        self.left = None
        self.right = None
        self.L = L
        self.R = R


class NumArray:

    def __init__(self, nums: List[int]):
        self.len = len(nums) - 1

        def build(nums, l, r):
            if l == r:
                return segmentTree(nums[l], l, r)

            root = segmentTree(0, l, r)
            m = l + (r - l) // 2
            root.left = build(nums, l, m)
            root.right = build(nums, m + 1, r)
            # print(root.left.sum, root.right.sum)
            root.sum = root.left.sum + root.right.sum
            # print(root.sum, l, r)
            return root

        self.root = build(nums, 0, len(nums) - 1)
        # print(self.root.sum)

    def update(self, index: int, val: int) -> None:
        cur = self.root
        l, r = 0, self.len

        def dfs(i, cur):
            if i == cur.L == cur.R:
                print(i, cur.L, val)
                cur.sum = val
                return cur
            l, r = cur.L, cur.R
            m = l + (r - l) // 2
            if i <= m:
                cur.left = dfs(i, cur.left)
            else:
                cur.right = dfs(i, cur.right)
            cur.sum = cur.left.sum + cur.right.sum
            # cur.sum = left + right
            return cur

        dfs(index, cur)
        # print(cur.sum)

    def sumRange(self, left: int, right: int) -> int:
        cur = self.root

        def dfs(left, right, cur):
            if cur.L == left and cur.R == right:
                return cur.sum

            l, r = cur.L, cur.R
            m = l + (r - l) // 2
            if right <= m:
                res = dfs(left, right, cur.left)
            elif left > m:
                res = dfs(left, right, cur.right)
            else:
                res = dfs(left, m, cur.left) + dfs(m + 1, right, cur.right)

            return res

        return dfs(left, right, cur)
