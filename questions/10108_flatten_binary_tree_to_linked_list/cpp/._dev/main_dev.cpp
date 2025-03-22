#include <vector>
#include <iostream>

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
};

// Function declarations

TreeNode* setup_question(int argc, char* argv[]);
void print_flattened_tree(TreeNode* root);

void flatten_binary_tree(TreeNode* root) {
    TreeNode* current = root;
    while (current) {
        if (current->left) {
            TreeNode* predecessor = current->left;
            while (predecessor->right) {
                predecessor = predecessor->right;
            }
            predecessor->right = current->right;
            current->right = current->left;
            current->left = nullptr;
        }
        current = current->right;
    }
}

int main(int argc, char* argv[]) {
    
    // Setup the binary tree
    TreeNode* root = setup_question(argc, argv);

    // Call the user function to flatten the binary tree
    flatten_binary_tree(root);

    // Print the flattened tree
    print_flattened_tree(root);

    return 0;
}