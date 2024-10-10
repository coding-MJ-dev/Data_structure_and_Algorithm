# 127. Word Ladder


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        dic = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]
                dic[pattern].append(w)

        count = 1
        visit = set()
        q = deque()
        q.append(beginWord)
        visit.add(beginWord)

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return count
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i + 1 :]
                    for nei in dic[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            count += 1

        return 0
