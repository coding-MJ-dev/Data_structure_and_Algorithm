// 946. Validate Stack Sequences

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int i = 0;
        for (int n : pushed) {
            st.push(n);
            while (!st.empty() && (st.top() == popped[i])) {
                i++;
                st.pop();
            }
        }
        return st.empty();
    }
};