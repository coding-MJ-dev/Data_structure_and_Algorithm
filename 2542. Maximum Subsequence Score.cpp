//2542. Maximum Subsequence Score

#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
    public:
        long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
            vector<pair<int, int>> pairs;
            int n = nums1.size();
    
            for (int i = 0; i < n; i++) {
                pairs.emplace_back(nums2[i], nums1[i]);
            }
            sort(pairs.rbegin(), pairs.rend());
    
            priority_queue<int, vector<int>, greater<int>> minHeap;
            long long curSum = 0, ans = 0;
    
            for (int i = 0; i < n; i++) {
                int num2 = pairs[i].first;
                int num1 = pairs[i].second;
    
                curSum += num1;
                minHeap.push(num1);
    
                if (minHeap.size() == k) {
                    ans = max(ans, curSum * num2);
                    curSum -= minHeap.top();
                    minHeap.pop();
                }
    
            }
            return ans;
    
        }
    };