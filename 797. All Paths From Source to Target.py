# 797. All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph)-1
        q = deque([(0, [0])]) # node, path(visit), 

        while q:
            node, path = q.popleft()
            
            if node == target:
                ans.append(path[:])
                continue
            else:
                for nei in graph[node]:
                    if nei and nei not in path:
                        q.append((nei, path+[nei]))
        
        return ans

        # def find_all_paths(cur_node: int, cur_path: List[int]):
        #     if cur_node == total_nodes - 1:
        #         all_paths.append(list(cur_path))
        #         return

        #     for node in adj_list[cur_node]:
        #         cur_path.append(node)
        #         find_all_paths(node, cur_path)
        #         cur_path.pop()

        # adj_list = graph
        # seen = set()
        # all_paths = []
        # total_nodes = len(graph)
        # find_all_paths(0, [0])
        # return all_paths