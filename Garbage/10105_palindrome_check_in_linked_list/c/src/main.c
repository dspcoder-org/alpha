#include "../inc/util.h"

bool isPalindrome(struct Linked_List* head) {
    // Write your code here
}

int main(){

    // Setup the linked list
    struct Linked_List* head = setup_question();
    
    // User function to check if the linked list is a palindrome
    bool result = isPalindrome(head); 

    // Print the result
    printf(result ? "true\n" : "false\n");
    
    return 0;
}