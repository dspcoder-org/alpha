#include <stdio.h>
#include <stdlib.h>

#define VERIFY(cond)   \
    if (!(cond)) {             \
        printf("._bad_input"); \
        exit(0);               \
    }

// Content of util.h

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

// Function prototypes
extern struct TreeNode* setup_question(int argc, char* argv[]);
extern void print_flattened_tree(struct TreeNode* root);

// end of util.h

struct TreeNode* buildTree(int arr[], int n) {
    if (n == 0) return NULL;

    struct TreeNode** nodes = (struct TreeNode**) malloc(n * sizeof(struct TreeNode*));
    for (int i = 0; i < n; i++) {
        nodes[i] = (struct TreeNode*) malloc(sizeof(struct TreeNode));
        nodes[i]->val = arr[i];
        nodes[i]->left = nodes[i]->right = NULL;
    }

    for (int i = 0; i < n; i++) {
        if (2 * i + 1 < n) nodes[i]->left = nodes[2 * i + 1];
        if (2 * i + 2 < n) nodes[i]->right = nodes[2 * i + 2];
    }

    struct TreeNode* root = nodes[0];
    free(nodes);
    return root;
}

void print_flattened_tree(struct TreeNode* root) {
    while (root) {
        printf("%d", root->val);
        if (root->right) {
            printf(" ");
        }
        root = root->right;
    }
    printf("\n");
}

struct TreeNode* setup_question(int argc, char* argv[]) {
    if (argc == 1) {
        int n, temp;
        
        // Input the number of elements
        VERIFY(((scanf("%d", &n)) > 0));

        // Create an array to store the node values
        int nodes[n];

        // Input the values into the array
        for (int i = 0; i < n; i++) {
            VERIFY(((scanf("%d", &nodes[i])) > 0));
        }

        VERIFY(((scanf("%d", &temp)) == EOF));

        // Build the binary tree
        struct TreeNode* root = buildTree(nodes, n);

        return root;
    } else {
        int n = atoi(argv[1]);
        int nodes[n];

        for (int i = 0; i < n; i++) {
            nodes[i] = atoi(argv[i+2]);
        }

        // Build the binary tree
        struct TreeNode* root = buildTree(nodes, n);

        return root;
    }
}