// 155. Min Stack

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


#include <stack>

class MinStack {
private:
    stack<int> st;
    stack<int> minst;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        st.push(val);
        if (minst.empty() || minst.top() > val) {
            minst.push(val);
        } else {
            minst.push(minst.top());
        }
    }
    
    void pop() {
        minst.pop();
        return st.pop();
    }
    
    int top() {
        return st.top();
        
    }
    
    int getMin() {
        return minst.top();
        
    }
};

