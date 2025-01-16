// 1514. Path with Maximum Probability


#include <vector>
#include <queue>
#include <unordered_map>
#include <functional>
#include <utility>
#include <limits>
using namespace std;



class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int, double>>> adj(n);
        for (int i = 0; i < edges.size(); i++) {
            int n1 = edges[i][0], n2 = edges[i][1];
            double prob = succProb[i];
            adj[n1].emplace_back(n2, prob); // making (n1, prob) object directly and put it in to place vs push_back : already existing object
            adj[n2].emplace_back(n1, prob);
        }

        // max heap q - prob, node
        priority_queue<pair<double, int>> pq;
        pq.emplace(1.0, start_node);
        
        vector<double> maxProb(n, 0.0);
        maxProb[start_node] = 1.0;

        while (!pq.empty()) {
            auto [prob, node] = pq.top();
            pq.pop();
            
            if (prob < maxProb[node]) continue;
            
            for (auto& [nei, nei_prob] : adj[node]) {
                double new_prob = prob * nei_prob;
                if (new_prob > maxProb[nei]) {
                    maxProb[nei] = new_prob;
                    pq.emplace(new_prob, nei);
                }
            }
        }

        return maxProb[end_node];
    }
};