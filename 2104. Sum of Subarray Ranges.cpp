//2104. Sum of Subarray Ranges

#include <vector>
#include <stack>

using namespace std;

class Solution {
    public:
        long long subArrayRanges(vector<int>& nums) {
            long long ans {0};
            int n = nums.size();
            stack<int> sm_st, lg_st;
    
            for (int right = 0; right < n+1; right++) {
                while (!sm_st.empty() && (right == n || nums[sm_st.top()] > nums[right])) {
                    int mid = sm_st.top();
                    sm_st.pop();
                    int left = !sm_st.empty() ? sm_st.top() : -1;
                    ans -= (long long)(right - mid) * (mid - left) * nums[mid];
                }
                sm_st.push(right);
            }
    
            for (int right = 0; right < n+1; right++) {
                while (!lg_st.empty() && (right == n || nums[lg_st.top()] < nums[right])) {
                    int mid = lg_st.top();
                    lg_st.pop();
                    int left = !lg_st.empty() ? lg_st.top() : -1;
                    ans += (long long)(right - mid) * (mid - left) * nums[mid];
                }
                lg_st.push(right);
            }
            return ans;
        }
    };
    
    