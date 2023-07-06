#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int x;
    struct Node* next;
} Node;

void insert_end(Node** root, int value){
    Node* newNode = malloc(sizeof(Node));
    if (newNode == NULL) exit(1);

    newNode->next = NULL;
    newNode->x = value;

    if (*root == NULL){
        *root = newNode;
        return;
    }
    Node* curr = *root;
    while(curr->next != NULL) curr = curr->next;
    curr->next = newNode;
}

int has_loop(Node* root){
    Node* slow = root;
    Node* fast = root;

    while(slow!=NULL && fast!=NULL && fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;

        if(slow==fast){
            return 1;
        }
    }
    return 0;
}

int main(){
    Node* root = NULL;
    /* Node* root = malloc(sizeof(Node));
    if (root == NULL) exit(2);
    
    root->x = 15;
    root->next = NULL; */

    insert_end(&root, -2);
    insert_end(&root, 11);
    insert_end(&root, 22);
    insert_end(&root, 6);
    insert_end(&root, 7);

    root->next->next->next->next->next = root->next;
    
    for (Node* curr = root; curr != NULL; curr = curr->next){
        printf("%d\n",curr->x);
    }
    // Deberíamos incluir una func que libere memoria
    return 0;
}