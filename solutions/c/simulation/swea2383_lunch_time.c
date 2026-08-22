#include<stdio.h>
#include<stdlib.h>

/*
 * 사람들이 어느 계단으로 가야 하는가? -> 2개의 선택지가 존재한다.
 * => 최대 사람을 고려해도 2^10 이기 때문에 완전탐색?
 *
 * 시간을 어떻게 계산하지?
 *  사람 3명이 있다고 가정 하자 => 사람1 = A / 사람2 = B / 사람3 = A
 *  3명이 계단은 다 골랐고 이제 시간을 계산해야 한다.
 *      매분마다 사람을 이동시키는 시뮬레이션? => 매 1분 마다 while문
 *      = 계단까지 거리만큼 이동 -> 1분 대기 -> 길이만큼 내려간다
 *          단, 계단 정원이 3명이라는 조건이 존재!
 *              => 도착시간을 모아서 정렬한 후에 먼저 온 사람을 넣는다.
 *                  1번 계단(6)에 도착한 사람들 : 4, 2, 7, 1 => 1, 2, 4, 7
 *              그러면 자리가 없다는 걸 어떻게 표현할 수 있을까?
 *                  4(idx=3)번 사람은 1(idx=0)번 사람의 시간을 봐야한다. = n번째 사람은 n-3번 사람의 시간을 봐야 한다.
 *
 */

#define MAX_PEOPLE 10
#define INF 99999999
#define STAIR_CAPACITY 3

int N;

int people[MAX_PEOPLE][2]; // 사람들의 위치 저장
int stairs[2][3]; // 각 계단의 정보 저장 - 위치 + 길이.

int people_cnt; // 사람 수
int selected_stair[MAX_PEOPLE]; // 사람들의 계단 선택

int answer;


// int compare(const void *a, const void *b)
// {
//     int left = *(const int *)a;
//     int right = *(const int *)b;
//
//     return left - right;
// }
//
//
/*
 * person_index번째 사람과 stair_index번재 계단 사이의 맨해튼 거리를 계산한다.
 */
int get_distance(int person_idx, int stair_idx)
{
    int person_row = people[person_idx][0];
    int person_col = people[person_idx][1];

    int stair_row = stairs[stair_idx][0];
    int stair_col = stairs[stair_idx][1];

    return abs(person_row - stair_row) + abs(person_col - stair_col);
}


int calculate_stair_time(int arrival[], int count, int stair_length)
{
    if (count == 0)
    {
        return 0;
    }

    qsort(arrival, count, sizeof(int), compare);

    int stair_finish[STAIR_CAPACITY] = {0, 0, 0};

    int time = 0;
    int next_person = 0;
    int completed = 0;

    while (completed < count)
    {
        for (int slot = 0; slot < STAIR_CAPACITY; slot++)
        {
            if (stair_finish[slot] == time)
            {
                stair_finish[slot] = 0;
                completed++;
            }
        }

        for (int slot = 0; slot < STAIR_CAPACITY; slot++)
        {

        }
    }



}




/*
 * 현재 계단 배정 상태에서 모든 사람이 내려가는 시간을 계산한다.
 */
int simulate(void)
{
    // dfs 확인
    printf("selected : ");
    for (int i = 0; i <people_cnt; i++)
    {
        printf("%d ", selected_stair[i]);
    }
    printf("\n");


    int arrival[2][MAX_PEOPLE]; // 사람들의 도착시간 보관을 위한 2차원 배열
    int count[2] = {0, 0}; // 각 게단을 선택한 사람의 수

    for (int i = 0; i < people_cnt; i++)
    {
        int stair_index = selected_stair[i]; // 선택한 계단 idx

        // 도착 시간 계산 후 저장
        arrival[stair_index][count[stair_index]] = get_distance(i, stair_index);

        count[stair_index]++;
    }

    printf("stair_ 1 : ");
    for (int i = 0; i < count[0]; i++)
    {
        printf("%d ", arrival[0][i]);
    }
    printf("\n");


    // 1번째 계단 고른 사람들의 시간
    int stair_time_0 = calculate_stair_time(arrival[0], count[0], stairs[0][2]);

    // // 2번째 계단 고른 사람들 시간
    // int stair_time_1 = calculate_stair_time();

}


void dfs(int person_index)
{
    if (person_index == people_cnt)
    {
        int result = simulate();

        if (result < answer)
        {
            answer = result;
        }

        return;
    }

    selected_stair[person_index] = 0;
    dfs(person_index + 1);

    selected_stair[person_index] = 1;
    dfs(person_index + 1);
}

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &N);

        people_cnt = 0;
        int stair_cnt = 0;

        for (int row = 0; row < N; row++)
        {
            for (int col = 0; col < N; col++)
            {
                int value;
                scanf("%d", &value);

                if (value == 1)
                {
                    people[people_cnt][0] = row;
                    people[people_cnt][1] = col;

                    people_cnt++;
                } else if (value >= 2)
                {
                    stairs[stair_cnt][0] = row;
                    stairs[stair_cnt][1] = col;
                    stairs[stair_cnt][2] = value;

                    stair_cnt++;
                }
            }
        }

        answer = INF;

        dfs(0);

        printf("#%d %d\n", test_case, answer);
    }

    return 0;
}