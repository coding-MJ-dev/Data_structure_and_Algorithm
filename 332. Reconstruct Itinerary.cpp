// 332. Reconstruct Itinerary
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
    public:
        vector<string> findItinerary(vector<vector<string>>& tickets) {
            unordered_map<string, vector<string>> map;
    
            for (auto& t : tickets) {
                map[t[0]].push_back(t[1]);
            }
    
            for (auto& [src, des] : map) {
                sort(des.rbegin(), des.rend());
            }
    
            vector<string> ans;
            travel("JFK", map, ans);
            reverse(ans.begin(), ans.end());
            return ans;
        }
    
    private:
        void travel(string node, unordered_map<string, vector<string>>& map, vector<string>& ans) {
            while (!map[node].empty()) {
                string next_node = map[node].back();
                map[node].pop_back();
                travel(next_node, map, ans);
            }
            ans.push_back(node);
        }
    };

