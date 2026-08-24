  /*
  같은 큐, 두 가지 설계
  ─────────────────────────────────────────────────────────────
  설계 A: 전역 변수      — 코딩테스트 표준. 짧고 실수가 적다
  설계 B: 구조체 + 포인터 — 실무 C 표준. 여러 개를 만들 수 있다

  컴파일: gcc -Wall queue-two-designs.c -o queue-demo
*/

#include <stdio.h>

#define MAX_N 100

typedef struct {
  int r, c;
} Point;

/* ══════════════════════════════════════════════════════════
   설계 A — 전역 변수
   큐가 프로그램에 딱 하나만 있으면 이게 가장 짧다.
   ══════════════════════════════════════════════════════════ */

Point g_queue[MAX_N * MAX_N];
int g_head = 0, g_tail = 0;

void a_push(int r, int c) {
  Point p = {r, c};
  g_queue[g_tail++] = p;
}

Point a_pop(void) { return g_queue[g_head++]; }

int a_is_empty(void) { return g_head == g_tail; }

/* ══════════════════════════════════════════════════════════
   설계 B — 구조체 + 포인터
   상태가 구조체 안에 모여 있고, 어떤 큐를 다루는지 함수
   시그니처에 드러난다. 큐를 두 개, 열 개 만들 수 있다.
   ══════════════════════════════════════════════════════════ */

typedef struct {
  Point items[MAX_N * MAX_N];
  int head;
  int tail;
} Queue;

/* q를 '포인터'로 받는 것이 핵심.
   Queue를 값으로 받으면 80KB를 복사하는 데다,
   head/tail 변경이 호출자에게 반영되지 않는다. */
void q_init(Queue *q) { q->head = q->tail = 0; }

void q_push(Queue *q, int r, int c) {
  Point p = {r, c};
  q->items[q->tail++] = p;
}

Point q_pop(Queue *q) { return q->items[q->head++]; }

int q_is_empty(const Queue *q) { return q->head == q->tail; }

/* ══════════════════════════════════════════════════════════ */

int main(void) {
  puts("── 설계 A: 전역 변수 ──");
  a_push(1, 1);
  a_push(2, 2);
  while (!a_is_empty()) {
    Point p = a_pop();
    printf("  (%d, %d)\n", p.r, p.c);
  }

  puts("\n── 설계 B: 구조체 ── (큐 두 개를 동시에)");
  Queue forward, backward; /* 전역 방식으로는 변수를 복사해야 하는 지점 */
  q_init(&forward);
  q_init(&backward);

  q_push(&forward, 0, 0);
  q_push(&backward, 9, 9);
  q_push(&forward, 0, 1);

  printf("  forward : ");
  while (!q_is_empty(&forward)) {
    Point p = q_pop(&forward);
    printf("(%d,%d) ", p.r, p.c);
  }
  printf("\n  backward: ");
  while (!q_is_empty(&backward)) {
    Point p = q_pop(&backward);
    printf("(%d,%d) ", p.r, p.c);
  }
  puts("");

  return 0;
}

/*
  ── 언제 무엇을 쓰나 ──────────────────────────────────────

  전역 (A)를 쓰는 경우:
    - 코딩테스트. 파일 하나, 큐 하나, 수명 30분
    - 큰 배열이 필요할 때 (아래 '스택 크기' 참고)
    - 0으로 자동 초기화되는 게 이득일 때 (visited, dist 배열)

  구조체 (B)를 쓰는 경우:
    - 같은 자료구조를 두 개 이상 써야 할 때
      (양방향 BFS, 0-1 BFS, 여러 그래프)
    - 코드를 재사용하거나 테스트할 때
    - 다른 사람이 읽을 코드. 함수 시그니처가 무엇을 건드리는지 말해준다

  ── 전역이 코테에서 유리한 기술적 이유 ────────────────────

  1) 스택 크기: 지역 변수는 스택에 잡힌다. 스택은 보통 1~8MB.
     int big[3000][3000] (36MB)을 main 안에 선언하면 즉시
     스택 오버플로. 전역이면 BSS 영역에 잡혀서 문제없다.

  2) 자동 0 초기화: 전역/static 변수는 0으로 초기화된다.
     지역 배열은 쓰레기값이다. visited[] 같은 배열을 전역으로
     두면 memset 없이 바로 쓸 수 있다.

  3) 인자 전달 실수가 없다: 넘길 게 없으면 잘못 넘길 일도 없다.
*/
