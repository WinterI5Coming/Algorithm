#include <stdio.h>
#include <stdlib.h>


// 노드 정의
typedef int element_type;
typedef struct tag_node {
    element_type data;
    struct tag_node* next_node;
} Node;


// 노드 생성
Node* create_node(int data) {

    Node* new_node = (Node*)malloc(sizeof(Node));

    new_node->data = data;
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


// 출력
void print_list(Node* head) {
    Node* current = head;
    int count = 0;

    while (current != NULL && (++count) <= 10) {
        printf("%d ", current->data);
        current = current->next_node;
    }
    printf("\n");
}



int main() {
    // freopen("input.txt", "r", stdin);



    int T = 10;

    for (int tc = 1; tc < T + 1; tc++) {

        int N; // 암호문의 개수
        scanf("%d", &N);

        // 더미 노드 생성
        Node* dummy = create_node(0);
        dummy->next_node = NULL;

        Node* tail = dummy;

        for (int i = 0; i < N; i++) {
            int code;
            scanf("%d", &code);

            Node* new_node = create_node(code);
            tail->next_node = new_node;
            tail = new_node;
        }

        int M;
        scanf("%d", &M);

        for (int i = 0; i < M; i++) {

            char cmd;
            scanf(" %c", &cmd);

            if (cmd == 'I') {

                int x, y; // x번째 다음에 y개의 암호문 삽입
                scanf("%d %d", &x, &y);

                // x번째 노드 찾기
                Node* after = get_node_at(dummy, x);

                for (int j = 0; j < y; j++) {
                    int code;
                    scanf("%d", &code);

                    Node* new_node = create_node(code);
                    new_node->next_node = after->next_node;
                    after->next_node = new_node;

                    after = new_node;
                }

            }
            else if (cmd == 'D') {

                int x, y; // x번째 바로 다음부터 y개의 암호문 삭제
                scanf("%d %d", &x, &y);

                // x번째 노드 찾기
                Node* after = get_node_at(dummy, x);
                Node* temp = NULL;

                for (int j = 0; j < y; j++) {
                    if (after->next_node == NULL) break;

                    temp = after->next_node;
                    after->next_node = temp->next_node;
                    free(temp);
                }

            }
            else if (cmd == 'A') {

                int y; // 암호문 맨 뒤에 y개의 암호문 덧붙인다
                scanf("%d", &y);

                // 일단 tail을 찾는다.
                Node* tail = dummy;
                while (tail != NULL && tail->next_node != NULL) {
                    tail = tail->next_node;
                }

                for (int j = 0; j < y; j++) {
                    int code;
                    scanf("%d", &code);

                    Node* new_node = create_node(code);
                    tail->next_node = new_node;
                    tail = new_node;
                }
            }
        }

        printf("#%d ", tc);
        print_list(dummy->next_node);
    }

    return 0;
}
