# 1626. Best Team With No Conflicts

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pair = [(x,y) for x, y in zip(ages, scores)]
        pair.sort()
        dp = [0] * (len(scores))
        # print(pair)
        for i in range(len(pair)-1, -1, -1):
            age, score = pair[i]
            dp[i] = score
            max_pre_score = 0
            for j in range(i+1, len(pair)):
                pre_age, pre_score = pair[j]
                if pre_age > age and pre_score < score:
                    continue
                max_pre_score = max(max_pre_score, dp[j])
            dp[i] += max_pre_score 
        # print(dp)
        return max(dp)