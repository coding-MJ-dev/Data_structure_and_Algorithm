# 406. Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
       res = []
        for p in sorted((-x[0], x[1]) for x in people):
            res.insert(p[1], [-p[0], p[1]])
        return res
