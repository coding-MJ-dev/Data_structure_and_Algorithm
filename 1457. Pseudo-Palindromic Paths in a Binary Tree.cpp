// 1457. Pseudo-Palindromic Paths in a Binary Tree


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    private:
        int dfs(TreeNode* node, int path) {
            if (!node) return 0;
    
            path ^= (1<< node->val);
    
            if (!node->left && !node->right) {
                return (__builtin_popcount(path) <= 1 ? 1 : 0);
            }
    
            return dfs(node->left, path) + dfs(node->right, path);
        }
    public:
        int pseudoPalindromicPaths (TreeNode* root) {
            return dfs(root, 0);
        }
    };