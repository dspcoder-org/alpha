#include <iostream>
#include <vector>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        std::cout << "._bad_input\n"; \
        exit(0);               \
    }

// Copy content of util.hpp
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

// Function to build a binary tree from an array
TreeNode* buildTree(int arr[], int n) {
    if (n == 0) return nullptr;

    std::vector<TreeNode*> nodes(n);
    for (int i = 0; i < n; ++i) {
        nodes[i] = new TreeNode(arr[i]);
    }

    for (int i = 0; i < n; ++i) {
        if (2 * i + 1 < n) nodes[i]->left = nodes[2 * i + 1];
        if (2 * i + 2 < n) nodes[i]->right = nodes[2 * i + 2];
    }

    return nodes[0];
}

// Function to print the flattened tree
void print_flattened_tree(TreeNode* root) {
    while (root) {
        std::cout << root->val;
        if (root->right) {
            std::cout << " ";
        }
        root = root->right;
    }
    std::cout << std::endl;
}

TreeNode* setup_question(int argc, char* argv[]) {
    if (argc == 1) {
        int n, temp;
        
        // Input the number of elements
        VERIFY((std::cin >> n));

        // Create an array to store the node values
        std::vector<int> nodes(n);

        // Input the values into the array
        for (int i = 0; i < n; i++) {
            VERIFY((std::cin >> nodes[i]));
        }

        VERIFY((std::cin >> temp).fail() == true);

        // Build the binary tree
        TreeNode* root = buildTree(nodes.data(), n);

        return root;
    } else {
        int n = std::stoi(argv[1]);
        std::vector<int> nodes(n);

        for (int i = 0; i < n; i++) {
            nodes[i] = std::stoi(argv[i+2]);
        }

        // Build the binary tree
        TreeNode* root = buildTree(nodes.data(), n);

        return root;
    }
}