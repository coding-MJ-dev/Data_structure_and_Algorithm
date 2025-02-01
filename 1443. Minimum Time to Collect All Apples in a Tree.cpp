//1443. Minimum Time to Collect All Apples in a Tree

class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        unordered_map<int, vector<int>> adj;

        for (auto& edge : edges){
            int s = edge[0], e = edge[1];
            adj[s].push_back(e);
            adj[e].push_back(s);
        }
        return dfs(0, -1, adj, hasApple); 
    }

private:
    int dfs(int node, int pre, unordered_map<int, vector<int>>& adj, vector<bool>& hasApple) {
        int time = 0;
        for (int nei : adj[node]) {
            if (nei == pre) continue;
            int child_time = dfs(nei, node, adj, hasApple);
            if (child_time > 0 || hasApple[nei]) {
                time += child_time + 2;
            }
        }
        return time;
    }

};