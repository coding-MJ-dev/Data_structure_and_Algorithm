# 275. H-Index II

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #3개를 받은게 3개 이상인가? 이를테면[5,5,5,5,5] 면 5를 받은게 5개 이상이니 값은 5
        n = len(citations)
        if len(citations) == 1:
            return 1 if citations[0] else 0
        if citations[0] >= n:
            return n

        n = len(citations)
        l, r= 0, n - 1, 
        ans = 0
        while l <= r:
            m = l + (r - l) // 2

            if citations[m] < n - m:
                l = m + 1
            else:
                r = m - 1
        
        return n-l
