// 1361. Validate Binary Tree Nodes

#include <vector>
#include <queue>
using namespace std;


class Solution {
    public:
        bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
            vector<int> roots(n, -1);
    
            for (int i = 0; i < n; i++) {
                if (leftChild[i] != -1){
                    if (roots[leftChild[i]] != -1) {
                        return false;
                    }
                    else {
                        roots[leftChild[i]] = i;
                    }
                }
            }
    
            for (int i = 0; i < n; i++) {
                if (rightChild[i] != -1){
                    if (roots[rightChild[i]] != -1) {
                        return false;
                    }
                    else {
                        roots[rightChild[i]] = i;
                    }
                }
            }
    
            int root = -1;
            int root_count = 0;
            for (int i = 0; i < n; i++) {
                if (roots[i] == -1) {
                    root = i;
                    root_count++;
                }
            }
    
            if (root == -1 || root_count > 1) return false;
            
            int count = 0;
            vector<bool> visit(n, false);
            queue<int> q;
            q.push(root);
            while (!q.empty()) {
                int node = q.front();
                q.pop();
                if (visit[node] == true) {return false;}
                visit[node] = true;
                count++;
                if (leftChild[node] != -1) {
                    q.push(leftChild[node]);
                }
                if (rightChild[node] != -1) {
                    q.push(rightChild[node]);
                }
            }
            return n == count;
    
        }
    };