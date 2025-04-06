#include "util.hpp"

int main(int argc, char* argv[]) {
    // Initialize the linked list using setup_question
    LinkedList* head = setup_question(argc, argv);

    // Detect cycle in the linked list using the user-defined function
    bool has_cycle = detect_cycle_in_linked_list(head);

    // Print the result
    std::cout << (has_cycle ? "true" : "false") << std::endl;

    // Free the memory allocated for the linked list
    delete_LinkedList(head);

    return 0;
}