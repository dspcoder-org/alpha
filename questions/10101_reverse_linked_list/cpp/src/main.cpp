#include "util.hpp"

int main(int argc, char* argv[]) {
    // Initialize the linked list using setup_question
    LinkedList* head = setup_question(argc, argv);

    // Reverse the linked list using the user-defined function
    reverse_Linked_list(&head);

    // Print the reversed linked list
    print_LinkedList(head);

    // Free the memory allocated for the linked list
    delete_LinkedList(head);

    return 0;
}