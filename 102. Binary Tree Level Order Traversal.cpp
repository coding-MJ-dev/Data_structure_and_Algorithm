// 102. Binary Tree Level Order Traversal

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {

        vector<vector<int>> ans;
        queue<TreeNode*> q;
        if (!root) {return ans;}
        q.push(root);
        while (!q.empty()) {
            int i = q.size();
            vector<int> cur;
            for (int j = 0; j < i; j++) {
                TreeNode* node = q.front();
                q.pop();
                cur.push_back(node->val);
                if (node->left != NULL) {
                    q.push(node->left);
                }
                if (node->right != NULL) {
                    q.push(node->right);
                }                                
            }
            ans.push_back(cur);
        }
        return ans;
    }
};


