# 721. Accounts Merge


class UnionFind:
    def __init__(self, n):
        self.p = {}
        self.rank = [1 for i in range(n)]
        for i in range(n):
            self.p[i] = i

    def find(self, n):
        p = self.p[n]
        while self.p[p] != p:
            self.p[p] = self.p[self.p[p]]
            p = self.p[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
            self.rank[p1] += 1
        else:
            self.p[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        names = []
        emailtoInd = {}
        for i, account in enumerate(accounts):
            names.append(account[0])
            for e in account[1:]:
                if e in emailtoInd:
                    uf.union(i, emailtoInd[e])
                    emailtoInd[e] = uf.find(i)
                else:
                    emailtoInd[e] = i

        ans = []
        IndtoEmail = defaultdict(list)
        for e, ind in emailtoInd.items():
            leader = uf.find(ind)
            IndtoEmail[leader].append(e)

        for ind, elist in IndtoEmail.items():
            ans.append([names[ind]] + sorted(elist))

        return ans
