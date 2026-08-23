/*
  N*N 지도에서 1은 집, 0은 빈 곳을 의미한다.
  상하좌우로 붙어있는 집들의 덩어리를 "단지"라고 부른다.

  단지의 개수와 각 단지의 집 수를 오름차순으로 출력한다.

  시간복잡도 : N의 최대값 25를 생각해보면 최대 625칸.
    모든 칸에서 BFS를 돌린다고 가정했을 때 log(N*N)?
    (0,0)부터 검사를 한다고 가저앟면


*/
#include <stdio.h>
#include <stdlib.h>

#define MAX_N 25

int grid[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
int N;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

typedef struct {
  int r;
  int c;
} Point;

Point que[MAX_N * MAX_N];
int head = 0;
int tail = 0;

void push(int r, int c) {
  Point new_point = {r, c};

  que[tail++] = new_point;
}

Point pop(void) { return que[head++]; }

int is_empty(void) { return head == tail; }

int bfs(int r, int c) {

  head = 0;
  tail = 0;

  int width = 1;
  visited[r][c] = 1;
  push(r, c);

  while (!is_empty()) {

    Point cur = pop();

    for (int d = 0; d < 4; d++) {
      int nr = cur.r + dr[d];
      int nc = cur.c + dc[d];

      if (0 <= nr && nr < N && 0 <= nc && nc < N) {
        if (grid[nr][nc] == 1 && visited[nr][nc] == -1) {
          visited[nr][nc] = 1;
          width++;
          push(nr, nc);
        }
      }
    }
  }

  return width;
}

int compare(const void *a, const void *b) {
  int x = *(const int *)a;
  int y = *(const int *)b;

  // 오름차순
  if (x < y)
    return -1;
  if (x > y)
    return 1;
  return 0;
}

int main(void) {

  // 입력 받기
  scanf("%d", &N);

  char buf[MAX_N + 1];
  for (int i = 0; i < N; i++) {
    scanf("%s", buf);
    for (int j = 0; j < N; j++) {
      grid[i][j] = buf[j] - '0';
      visited[i][j] = -1;
    }
  }

  int complex_cnt = 0;
  int complexes[MAX_N * MAX_N];

  // 각 점을 순회하면서 단지가 존재하는지 확인한다.
  for (int r = 0; r < N; r++) {
    for (int c = 0; c < N; c++) {

      if (grid[r][c] == 1 && visited[r][c] == -1) {
        complexes[complex_cnt] = bfs(r, c);
        complex_cnt++;
      }
    }
  }

  qsort(complexes, complex_cnt, sizeof(int), compare);

  printf("%d\n", complex_cnt);
  for (int i = 0; i < complex_cnt; i++) {
    printf("%d\n", complexes[i]);
  }

  return 0;
}
