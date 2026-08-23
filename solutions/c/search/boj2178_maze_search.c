/*
  질문 1. 최단 경로 문제가 어떤 문제인지는 모르겠다. 그러나 일반적으로 최단 경로를 찾는 문제에서
  DFS, BFS 모든 방법이 가능하긴 하다. 그러나 시간 복잡도를 고려해서 BFS를 적용하는 것이 일반적으로
  바람직하다. DFS는 깊이 우선 탐색이라 한 길을 먼저 끝까지 가본 다음에 다른 경로를 고려하기 때문에
  시간이 지나치게 많이 걸리기 때문이다.

  DFS가 도착칸에 처음 도달한 순간 그 거리가 최단이라고 보장할 수 없다. 왜냐하면 각 단계에서 내가
  가야하는 갈림길 중에서 단 한 가지의 선택만을 해서 끝까지 와본, 단 한 경우만을 고려한 것이기 때문에
  내가 이전에 다른 경로를 선택했다면? 이라는 걸 고려하기 위해 우리는 백트래킹이라는 것을 진행해야
  한다. 반대로 BFS는 거리가 같은 단계의 노드들을 같은 단계에서 고려하게 된다. 즉 a에서 시작하고 b,
  c가 큐에 들어가있다고 하면 b,c는 모드 거리가 2인 노드들이다. 여기서 b,c 모두 빠지면 b는 x, c는 d가
  들어가고 목적지는 x라고 한다면, 다음 단계에 c가 d를 들러 x를 갈 수 있다고 한들 b에서 x에 도착해서
  큐가 아예 끝나버리면 루프가 끝이난다. 즉, 한 번 목적지에 도달하게 되면 다른 경로는 고려하지
  않는다.

  질문 2. BFS에서 방문 표시는 큐에서 꺼내고 방문하지 않았다면 그때 방문 표시를 하고 내가 가야할 다음
  경로를 다시 큐에 넣는다.

  그렇네 너가 작성해준 손으로 따라가라는 예를 들어보니까 호학실히 문제점이 존재한 것 같다. 큐에서
  빼는 것이 아니라 넣을 때 방문처리를 해줘야 할 것 같다..

  */

#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100

typedef struct {
  int r;
  int c;
} Point;

int N, M;
int maze[MAX_N][MAX_N];
int dist[MAX_N][MAX_N];

Point queue[MAX_N * MAX_N];
int head = 0;
int tail = 0;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

void push(int r, int c) {
  // 먼저 Point 만든다.
  Point new_point = {r, c};

  /*
    head = 0, tail = 0 => tail에 값 넣고 tail++
    haed = 0, tail = 1 => tail에 값 넣고 tail++
    첫번째 값 빠졌다. head = 0에서 pop, head++
    두번째 값 빠졌다. head = 1에서 pop, head++

    => head = 2, tail = 2 / 즉, 두 값이 같다는 건 que 비어있다는 것
  */

  queue[tail++] = new_point;
}

Point pop() { return queue[head++]; }

int is_empty() { return head == tail; }

int bfs(void) {

  dist[0][0] = 1;
  push(0, 0);

  while (!is_empty()) {
    Point cur = pop();

    for (int dir = 0; dir < 4; dir++) {
      int nr = cur.r + dr[dir];
      int nc = cur.c + dc[dir];
      if (0 <= nr && nr < N && 0 <= nc && nc < M) {
        if (maze[nr][nc] != 0 && dist[nr][nc] == -1) {
          dist[nr][nc] = dist[cur.r][cur.c] + 1;
          push(nr, nc);
        }
      }
    }
  }

  return dist[N - 1][M - 1];
}

int main(void) {

  // push(1, 1);
  // push(1, 3);
  // push(2, 4);

  // while (!is_empty()) {
  //   Point pop_point = pop();
  //   printf("popped : %d %d \n", pop_point.r, pop_point.c);
  // }

  // 입력받기
  scanf("%d %d", &N, &M);

  char buf[MAX_N + 1];

  for (int i = 0; i < N; i++) {
    scanf("%s", buf);
    for (int j = 0; j < M; j++) {
      maze[i][j] = buf[j] - '0';
      dist[i][j] = -1;
    }
  }

  printf("%d\n", bfs());

  return 0;
}