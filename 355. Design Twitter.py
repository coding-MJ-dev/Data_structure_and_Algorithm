# 355. Design Twitter
class Twitter:

    def __init__(self):
        self.time = 0  # time
        self.uid = defaultdict(list)  # {followerId: [followeeId1, followeeId2...]}
        self.id2t = defaultdict(list)  # {userId: (time(tid), tweetId)}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.id2t[userId].append((-1 * self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []

        for f in uid[userId]:
            if self.id2t[f]:
                for i in range(min(len(self.id2t[f], 10))):
                    hp.heappush(self.id2t[f][-(i + 1)])

        ans = []
        for _ in range(10):
            time, tw = heappop(hp)
            ans.append(tw)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.uid:
            self.uid[followeeId] = followeeId
        if followerId not in self.uid[followeeId]:
            self.uid[followeeId].append(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.uid[followeeId]:
            self.uid[followeeId].remove(followerId)
