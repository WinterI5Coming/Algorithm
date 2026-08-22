#include <stdio.h>
#include <stdlib.h>


// 노드 정의
typedef int element_type;
typedef struct tag_node {
    element_type data;
    struct tag_node* prev_node;
    struct tag_node* next_node;
} Node;


// 노드 생성
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));

    new_node->data = data;
    new_node->prev_node = NULL;
    new_node->next_node = NULL;

    return new_node;
}


// 노드 탐색
Node* get_node_at(Node* head, int index) {
    Node* current = head;

    for (int i = 0; i < index && current != NULL; i++) {
        current = current->next_node;
    }

    return current;
}


// 노드 출력


int main() {

    int T;
    scanf("%d", &T);

    for (int tc = 1; tc < T + 1; tc++) {
        int N, M, L; // N = 수열 길이, M = 추가 횟수, L = 출력할 인덱스
        scanf("%d %d %d", &N, &M, &L);

        Node* dummy = create_node(0);
        dummy->prev_node = NULL;
        dummy->next_node = NULL;

        // 연결 리스트 구현
        Node* tail = dummy;

        for (int i = 0; i < N; i++) {
            int num;
            scanf("%d", &num);

            Node* new_node = create_node(num);
            tail->next_node = new_node;
            new_node->prev_node = tail;
            tail = new_node;
        }

        // 명령 실행
        for (int i = 0; i < M; i++) {
            char cmd;
            scanf(" %c", &cmd);

            if (cmd == 'I') {
                int x, y; // x번 인덱스 앞에 y 추가
                scanf("%d %d", &x, &y);

                Node* before = get_node_at(dummy, x + 1);
                Node* new_node = create_node(y);

                if (before == NULL) {
                    tail->next_node = new_node;
                    new_node->prev_node = tail;
                    tail = new_node;
                } else {
                    new_node->next_node = before;
                    new_node->prev_node = before->prev_node;

                    before->prev_node->next_node = new_node;
                    before->prev_node = new_node;
                }

            }
            else if (cmd == 'D') {
                int x; // x번 인덱스 노드 삭제
                scanf("%d", &x);

                Node* remove = get_node_at(dummy, x + 1);

                if (remove == NULL) {
                    continue;
                }

                remove->prev_node->next_node = remove->next_node;

                if (remove->next_node != NULL) {
                    remove->next_node->prev_node = remove->prev_node;
                } else {
                    tail = remove->prev_node;
                }

                free(remove);
            }
            else if (cmd == 'C') {
                int x, y; // x번 인덱스 자리를 y로 교체
                scanf("%d %d", &x, &y);

                Node* replace = get_node_at(dummy, x + 1);

                if (replace != NULL) {
                    replace->data = y;
                }
            }

        }

        Node* result = get_node_at(dummy, L + 1);

        printf("#%d ", tc);

        if (result == NULL) {
            printf("-1");
        } else {
            printf("%d", result->data);
        }
        printf("\n");
    }


    return 0;
}
