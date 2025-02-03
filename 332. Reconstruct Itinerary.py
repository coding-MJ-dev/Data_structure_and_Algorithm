# 332. Reconstruct Itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets, reverse = True):
            adj[src].append(dest)
        
        ans = []
        def dfs(node):
            while adj[node]:
                next_node = adj[node].pop()
                dfs(next_node)
            ans.append(node)
        
        dfs('JFK')
        return ans[::-1]

        # graph = defaultdict(list)

        # # Build the graph as a priority queue (min-heap) for lexical order
        # for src, dest in sorted(tickets):
        #     graph[src].append(dest)

        # result = []

        # def dfs(node):
        #     while graph[node]:
        #         next_dest = graph[node].pop(0)
        #         dfs(next_dest)
        #     result.append(node)

        # # Start the journey from 'JFK'
        # dfs('JFK')

        # # Since the result is constructed in reverse order, reverse it
        # return result[::-1]