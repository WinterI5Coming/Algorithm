#include <stdio.h>
#include <stdlib.h>


// 노드 정의
typedef int elementType;

typedef struct tagNode {

    elementType data;
    struct tagNode* nextNode;
} Node;


// 노드 생성
Node* createNode(elementType newData) {

    Node* newNode = malloc(sizeof(Node));

    newNode->data = newData;
    newNode->nextNode = NULL;

    // 주소 반환
    return newNode;
}


// 노드 추가
void appendNode(Node** head, Node* newNode) {
    
    if ((*head) == NULL) {
        // 리스트 자체가 비어있는 경우 => head 자체가 NULL 일 것.
        
        *head = newNode;

    } else {
        // 빈 리스트가 아닌 경우
        // => 마지막 노드(tail)를 찾아야 한다. 마지막 노드는 nextNode가 NULL인 노드
        
        Node* tail = (*head);
        while (tail->nextNode != NULL) {

            tail = tail->nextNode;
        }

        // tail을 찾았다면, 해당 노드에 연결한다.
        tail->nextNode = newNode;
        
    }
}


// 노드 탐색
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
        // 지우고자 하는 노드의 주소값이 head의 주소값과 같은 경우
        // = 첫 노드를 지우려고 하는 경우

        *head = remove->nextNode;

    } else {
        // 아닌 경우 => 지우려고 하는 노드(remove)의 이전 노드를 찾아야 한다.
        
        Node* current = (*head);
        while (current != NULL && current->nextNode != remove) {

            current = current->nextNode;

        }

        if (current != NULL) {

            current->nextNode = remove->nextNode;

        }

    }

}


// 노드 삽입
void insertNode(Node* current, Node* newNode) {

    // current 뒤에 삽입
    // 삽입하고자 하는 노드(newNode)의 다음 노드를 먼저 할당해 주어야 한다.

    // 그렇지 않고 current의 nextNode에 먼저 새 노드의 주소값을 할당하면, 
    // => 기존에 current 노드의 nextNode를 새 노드의 nextNode에 연결해주어야 하는데, 
    //      이미 덮어씌워져서 연결이 불가능해진다.

    newNode->nextNode = current->nextNode;
    current->nextNode = newNode;
    
}


// linkedList 출력
void printLinkedList(Node* head) {

    Node* current = head;
    while (current != NULL) {

        printf("%d -> ", current->data);
        current = current->nextNode;
    }
    printf("\n");

}


int main() {

    // 변수명은 linkedList 이지만 head 역할을 할 것이다.
    // => 즉, 첫 노드 (head)의 주소값을 가르키는 것
    Node* linkedList = NULL;

    Node* node_1 = createNode(20);
    Node* node_2 = createNode(37);
    Node* node_3 = createNode(55);
    Node* node_4 = createNode(68);
    Node* node_5 = createNode(73);
    Node* node_6 = createNode(89);
    Node* node_7 = createNode(91);

    appendNode(&linkedList, node_1);
    appendNode(&linkedList, node_2);
    appendNode(&linkedList, node_3);
    appendNode(&linkedList, node_4);
    appendNode(&linkedList, node_5);
    appendNode(&linkedList, node_6);
    appendNode(&linkedList, node_7);


    // 4번째 노드 가져오기
    Node* fourthNode = getNodeAt(linkedList, 4);
    printf("fourthNode = %d\n", fourthNode->data);

    printLinkedList(linkedList);

    removeNode(&linkedList, fourthNode);

    printLinkedList(linkedList);


    // 3번째 노드 뒤에 삽입
    Node* node_8 = createNode(101);
    insertNode(getNodeAt(linkedList, 3), node_8);

    printLinkedList(linkedList);
    
    
    return 0;
}