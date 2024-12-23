# 433. Minimum Genetic Mutation

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        pool = ['A', 'C', 'G', 'T']
        bank = set(bank)
        if endGene not in bank:
            return -1

        if startGene == endGene:
            return 0
        
        q = deque([(startGene, 0)])
        while q:
            g, step = q.popleft()
            for i in range(len(g)):
                for p in pool:
                    if p == g[i]:
                        continue
                    new_g = g[:i] + p + g[i+1:]
                    if new_g == endGene:
                        return step + 1
                    if new_g in bank:
                        q.append((new_g, step + 1))
                        bank.remove(new_g)
        return -1