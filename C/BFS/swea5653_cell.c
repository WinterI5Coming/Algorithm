/*
줄기세포 배양 시뮬레이션 프로그램을 만든다.
일정 시간 동안 배양한 후 살아있는 줄기세포의 개수를 계산한다.

줄기세포
    생명력이 X라면 X시간 동안 비활성 상태
    X시간이 지나면 활성 상태
    활성 상태가 된 첫 1시간 동안 상하좌우로 번식
    활성 상태로 X시간이 지나면 사망

번식
    이미 세포가 존재했던 위치에는 번식할 수 없다.
    같은 위치로 동시에 번식하면 생명력이 높은 세포가 차지한다.
*/

#include <stdio.h>
#include <string.h>

#define GRID_SIZE 700
#define OFFSET 350 // 음수 좌표가 발생하지 않도록 전체 좌표를 오른쪽 아래로 이동시키기 위함의 offset 값 지정

// 해당 위치를 차지한 세포의 생명력
int grid[GRID_SIZE][GRID_SIZE];

// 해당 위치의 세포가 생성된 시간
int birth_time[GRID_SIZE][GRID_SIZE];

// 이번 1시간 동안 번식할 세포 후보
int next_grid[GRID_SIZE][GRID_SIZE];

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        int N;
        int M;
        int K;

        scanf("%d %d %d", &N, &M, &K);

        // 테스트 케이스마다 배열 초기화
        memset(grid, 0, sizeof(grid));
        memset(birth_time, 0, sizeof(birth_time));

        // 초기 줄기세포 입력
        for (int row = 0; row < N; row++)
        {
            for (int col = 0; col < M; col++)
            {
                int life;
                scanf("%d", &life);

                if (life != 0)
                {
                    grid[OFFSET + row][OFFSET + col] = life;
                    birth_time[OFFSET + row][OFFSET + col] = 0;
                }
            }
        }

        const int dir_row[4] = {-1, 1, 0, 0};
        const int dir_col[4] = {0, 0, -1, 1};

        /*
        time부터 time + 1까지의 변화를 처리한다.

        K시간 후까지만 확인해야 하므로
        time은 0부터 K - 1까지만 진행한다.
        */
        for (int time = 0; time < K; time++)
        {
            // 현재 시간의 번식 후보 초기화
            memset(next_grid, 0, sizeof(next_grid));

            int row_start = OFFSET - time;
            int row_end = OFFSET + N - 1 + time;

            int col_start = OFFSET - time;
            int col_end = OFFSET + M - 1 + time;

            // 현재까지 세포가 존재할 수 있는 범위를 순회한다.
            for (int row = row_start; row <= row_end; row++)
            {
                for (int col = col_start; col <= col_end; col++)
                {
                    // 세포가 없는 위치
                    if (grid[row][col] == 0)
                    {
                        continue;
                    }

                    int life = grid[row][col];
                    int born = birth_time[row][col];

                    /*
                    born 시간에 생성된 생명력 life인 세포는
                    born + life 시간에 활성화된다.

                    활성화된 첫 1시간 동안만 번식한다.
                    */
                    if (born + life != time)
                    {
                        continue;
                    }

                    // 상하좌우로 번식
                    for (int dir = 0; dir < 4; dir++)
                    {
                        int next_row = row + dir_row[dir];
                        int next_col = col + dir_col[dir];

                        // 배열 범위 확인
                        if (next_row < 0 ||
                            next_row >= GRID_SIZE ||
                            next_col < 0 ||
                            next_col >= GRID_SIZE)
                        {
                            continue;
                        }

                        /*
                        죽은 세포도 grid에 남아 있으므로
                        grid 값이 0이 아니면 번식할 수 없다.
                        */
                        if (grid[next_row][next_col] != 0)
                        {
                            continue;
                        }

                        /*
                        같은 위치로 여러 세포가 번식하면
                        생명력이 가장 높은 세포를 남긴다.
                        */
                        if (next_grid[next_row][next_col] < life)
                        {
                            next_grid[next_row][next_col] = life;
                        }
                    }
                }
            }

            /*
            모든 번식 경쟁이 끝난 후 한꺼번에 grid에 반영한다.

            번식은 time부터 time + 1까지 진행되므로
            새 세포의 생성 시간은 time + 1이다.
            */
            int next_row_start = OFFSET - (time + 1);
            int next_row_end = OFFSET + N - 1 + (time + 1);

            int next_col_start = OFFSET - (time + 1);
            int next_col_end = OFFSET + M - 1 + (time + 1);

            for (int row = next_row_start; row <= next_row_end; row++)
            {
                for (int col = next_col_start; col <= next_col_end; col++)
                {
                    if (next_grid[row][col] == 0)
                    {
                        continue;
                    }

                    grid[row][col] = next_grid[row][col];
                    birth_time[row][col] = time + 1;
                }
            }
        }

        // K시간 후 살아있는 세포의 개수 계산
        int answer = 0;

        int row_start = OFFSET - K;
        int row_end = OFFSET + N - 1 + K;

        int col_start = OFFSET - K;
        int col_end = OFFSET + M - 1 + K;

        for (int row = row_start; row <= row_end; row++)
        {
            for (int col = col_start; col <= col_end; col++)
            {
                if (grid[row][col] == 0)
                {
                    continue;
                }

                int life = grid[row][col];
                int born = birth_time[row][col];

                /*
                X 시간 동안 비활성 + X 시간 동안 활성 = 총 2X 시간 동안 살아 있다.
                => 정리하면 아래와 같다.

                born -> 비활성 상태 X시간 -> born + X -> 활성 상태 X시간 -> born + 2X -> 사망
                */
                int death_time = born + 2 * life;

                if (K < death_time)
                {
                    answer++;
                }
            }
        }

        printf("#%d %d\n", tc, answer);
    }

    return 0;
}