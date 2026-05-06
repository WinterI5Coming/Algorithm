#include <stdio.h>
#include <stdlib.h>


// 노드 정의
typedef int elementType;

typedef struct tagNode {

    elementType data;
    struct tagNode* prevNode;
    struct tagNode* nextNode;

} Node;


// 노드 생성
Node* createNode(int data) {

    Node* newNode = malloc(sizeof(Node));

    newNode->data = data;
    newNode->prevNode = NULL;
    newNode->nextNode = NULL;

    return newNode;
}


// 노드 추가
void appendNode(Node** head, Node* newNode) {

    if ((*head) == NULL) {
        // 빈 리스트인 경우
        (*head) = newNode;

    } else {
        // 끝 노드(tail) 을 찾는다
        Node* tail = (*head);
        while (tail != NULL && tail->nextNode != NULL) {

            tail = tail->nextNode;

        }

        // 찾았다면, 끝 노드와 새로운 노드를 서로 연결한다.
        tail->nextNode = newNode;
        newNode->prevNode = tail;

    }

}


// 노드 탐색 => linkedList 와 동일
Node* getNodeAt(Node* head, int location) {

    Node* current = head;
    while (current != NULL && (--location) > 0) {

        current = current->nextNode;

    }

    return current;
}


// 노드 삭제
void removeNode(Node** head, Node* remove) {

    if ((*head) == remove) {

        *head = remove->nextNode;
        
        // 삭제후 삽입한 노드가 값이 존재하는 경우
        if ((*head) != NULL) {
            (*head)->prevNode = NULL;
        }

        // 삭제후 삽입한 노드도 값이 없는 경우
        (*head)->prevNode = NULL;
        (*head)->nextNode = NULL;

    } else {

        Node* temp = remove;

        if (remove->prevNode != NULL) {
            // 지우려고 하는 노드의 이전 값이 존재하는 경우 = 연결되어 있는 이전 노드가 존재하는 경우
            // => 이전 노드의 nextNode를 remove 노드의 nextNode와 연결한다.
            remove->prevNode->nextNode = temp->nextNode;
        }

        if (remove->nextNode != NULL) {
            // 지우려고 하는 노드의 다음 값이 존재하는 경우 = 연결되어 있는 다음 노드가 존재하는 경우
            // => 다음 노드의 prevNode를 remove 노드의 prevNode와 연결한다.
            remove->nextNode->prevNode = temp->prevNode;
        } 

        remove->prevNode = NULL;
        remove->nextNode = NULL;

    }
}


// 노드 삽입
void insertNode(Node* current, Node* newNode) {

    // 삽입하려는 노드(newNode)의 nextNode(=> current->nextNode), prevNode(=> current) 값 할당
    newNode->nextNode = current->nextNode;
    newNode->prevNode = current;

    if (current->nextNode != NULL) {
        // current 노드의 다음노드가 존재하는 경우
        // => 해당 노드의 prevNode도 newNode와 연결해주어야 한다.
        current->nextNode->prevNode = newNode;
    }
    
    current->nextNode = newNode;
}


// doubleLinkedList 출력
void printDoubleLinkedList(Node* head) {

    Node* current = head;
    while (current != NULL) {

        printf("%d -> ", current->data);
        current = current->nextNode;
    }
    printf("\n");

}


int main() {


    Node* double_linked_list = NULL;

    Node* node_1 = createNode(7);
    Node* node_2 = createNode(13);
    Node* node_3 = createNode(27);
    Node* node_4 = createNode(39);


    appendNode(&double_linked_list, node_1);
    appendNode(&double_linked_list, node_2);
    appendNode(&double_linked_list, node_3);
    appendNode(&double_linked_list, node_4);

    printDoubleLinkedList(double_linked_list);


    return 0;
}