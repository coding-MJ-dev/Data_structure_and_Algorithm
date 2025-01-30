// 652. Find Duplicate Subtrees

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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> subTreeMap;
        vector<TreeNode*> ans;
        serialize(root, subTreeMap, ans);
        return ans;
    }

private:
    string serialize(TreeNode* node,  unordered_map<string, int>& subTreeMap, vector<TreeNode*>& ans) {
        if (!node) return "#";

        string val = to_string(node->val) + "," + serialize(node->left, subTreeMap, ans) + "," + serialize(node->right, subTreeMap, ans);
        subTreeMap[val]++;
        if (subTreeMap[val] == 2) {
            ans.push_back(node);
        }
        return val;
    }

};