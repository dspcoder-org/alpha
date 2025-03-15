#include "util.h"
#include <stdbool.h>

bool is_palindrome(struct Linked_List* head) {
    // Write your code here
}

int main(int argc, char* argv[]) {

    // Setup the linked list
    struct Linked_List* head = setup_question(argc, argv);
    
    // User function to check if the linked list is a palindrome
    bool result = is_palindrome(head); 

    // Print the result
    printf(result ? "true\n" : "false\n");
    
    return 0;
}