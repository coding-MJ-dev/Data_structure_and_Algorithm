// 95. Unique Binary Search Trees II


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
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
    private:
        vector<TreeNode*> buildTrees(int left, int right, unordered_map<int, vector<TreeNode*>>& dic) {
            if (left > right) {
                return {nullptr};
            }
            
            int key = left * 100 + right;
            if (dic.count(key) > 0) {
                return dic[key];
            }
            if (left == right) {
                dic[key] = {new TreeNode(left)};
                return dic[key];
            }
    
            // vector<TreeNode*> newTrees;
            for (int root = left; root <= right; root++) {
                vector<TreeNode*> leftTrees = buildTrees(left, root-1, dic);
                vector<TreeNode*> rightTrees = buildTrees(root+1, right, dic);
                for (auto leftTree: leftTrees) {
                    for (auto rightTree: rightTrees) {
                        dic[key].push_back(new TreeNode(root, leftTree, rightTree));
                    }
                }
            }
            // dic[key] = newTrees;
            return dic[key];
        }
    
    public:
        vector<TreeNode*> generateTrees(int n) {
            unordered_map<int, vector<TreeNode*>> dic;
            return buildTrees(1, n, dic);
    
        }
    };
    






// class Solution {
//     struct TreeNode {
//         int val;
//         TreeNode *left;
//         TreeNode *right;
//         TreeNode() : val(0), left(nullptr), right(nullptr) {}
//         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//     };
//     private:
//         vector<TreeNode*> makeT(int left, int right, unordered_map<int, vector<TreeNode*>>& dic) {
//             if (left > right) return {nullptr};
//             int key = left * 100 + right;
//             if (dic.count(key)) return dic[key];
    
//             vector<TreeNode*> allTrees;
//             for (int rootVal = left; rootVal <= right; rootVal++) {
//                 vector<TreeNode*> leftTrees = makeT(left, rootVal - 1, dic);
//                 vector<TreeNode*> rightTrees = makeT(rootVal + 1, right, dic);
    
//                 for (TreeNode* l : leftTrees) {
//                     for (TreeNode* r : rightTrees) {
//                         TreeNode* root = new TreeNode(rootVal, l, r);
//                         allTrees.push_back(root);
//                     }
//                 }
//             }
//             dic[key] = allTrees;
//             return allTrees;
//         }
//     public:
//         vector<TreeNode*> generateTrees(int n) {
//             if (n == 0) return {};
//             unordered_map<int, vector<TreeNode*>> dic;
//             return makeT(1, n, dic);
//         }
//     };