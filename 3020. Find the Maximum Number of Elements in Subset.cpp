// 3020. Find the Maximum Number of Elements in Subset

#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;


class Solution {
    public:
        int maximumLength(vector<int>& nums) {
            unordered_map<long long, int> dic;
            int ans {0};
    
            for (int n: nums) {
                dic[n]++;
            }
    
            for (auto& [n, freq] : dic) {
                int cur = 0;
                if (n == 1) {
                    cur = dic[n] % 2 ? dic[n] : dic[n] - 1; 
                }
                else {
                    long long num = n;
                    while (dic.count(num*num) && dic[num] >= 2 && num <= 1e9) {
                        cur += 2;
                        num *= num;
                    }
                    cur += 1;
                }
                ans = max(cur, ans);
            }
            return ans;
        }
    };
    