#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

/*
    qsort에 전달하는 함수는 항상 동일한 질문을 한다 = a가 b 앞에 있는가?
        - 맞다 = 음수
        - 아니다 = 양수

        오름차순의 경우,
            - a < b : a가 앞에 있는 것이 맞기 때문에 음수
            - a > b : a가 뒤에 있어야 하기 때문에 양수

        내림차순의 경우,
            - a < b : a가 뒤에 있어야 하기 때문에 양수
            - a > b : a가 앞에 있는 것이 맞기 때문에 음수
*/
int compare(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;

    // 오름차순
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {

    int N;
    scanf("%d", &N);

    int *cookies = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &cookies[i]);
    }

    // 정렬
    qsort(cookies, N, sizeof(int), compare);


    /*
        시작지점을 찾아주어야 한다.
        문제에서는 시작점을 0 이라고 했지만,
            정렬한 현재 상황 (ex. -11 -4 -1 2)에서 시작 지점은
            idx로 따졌을 때 2와 3 사이이다.

        그걸 우리는 투 포인터를 사용해서 푼다.
    */
    int right = 0;
    while (right < N && cookies[right] < 0) {
        right++;
    }
    int left = right - 1;

    long long cur_pos = 0;
    long long answer = 0;

    // -11 -4 -1 2 , right = 3 left = 2
    while (left >= 0 || right < N) {

        /*
            쿠키 하나 위치의 최대 값은 1,000,000,000 이다.
                근데 C에서 int 최대값은 2,000,000,000 정도이므로 오버플로우 발생한다.

            따라서 long long 타입 사용. (long 타입은 환경에 따라 크기므로 불확실...)
        */
        long long left_dist = LLONG_MAX;
        long long right_dist = LLONG_MAX;

        if (left >= 0) {
            left_dist = llabs((long long)cookies[left] - cur_pos);
        }

        if (right < N) {
            right_dist = llabs((long long)cookies[right] - cur_pos);
        }

        if (left_dist <= right_dist) {
            answer += left_dist;
            cur_pos = cookies[left];
            left--;
        } else {
            answer += right_dist;
            cur_pos = cookies[right];
            right++;
        }


    }

    printf("%lld\n", answer);

    free(cookies);

    return 0;
}
