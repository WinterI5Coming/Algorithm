#include <assert.h>
#include <stdio.h>

#define MAX_N 100

static int grid[MAX_N][MAX_N];
static int N;
static int M;
static const int dr[4] = {-1, 1, 0, 0};
static const int dc[4] = {0, 0, -1, 1};

typedef struct {
  int r;
  int c;
} Point;

typedef struct {
  Point items[MAX_N * MAX_N];
  int top;
} Stack;

void stack_init(Stack *stack);
int stack_is_empty(const Stack *stack);
void stack_push(Stack *stack, Point point);
int stack_pop(Stack *stack, Point *out);

void stack_init(Stack *stack) { stack->top = 0; }

int stack_is_empty(const Stack *stack) { return stack->top == 0; }

void stack_push(Stack *stack, Point point) { stack->items[stack->top++] = point; }

int stack_pop(Stack *stack, Point *out) {
  if (stack_is_empty(stack)) {
    return 0;
  }

  *out = stack->items[--stack->top];
  return 1;
}

static void assert_point(Point actual, int expected_r, int expected_c) {
  assert(actual.r == expected_r);
  assert(actual.c == expected_c);
}

int dfs_iterative(int r, int c) {
  Stack stack;
  Point cur = {r, c};
  int count = 1;

  stack_init(&stack);
  grid[r][c] = 0;
  stack_push(&stack, cur);

  while (stack_pop(&stack, &cur)) {
    for (int d = 0; d < 4; d++) {
      int nr = cur.r + dr[d];
      int nc = cur.c + dc[d];

      if (0 <= nr && nr < N && 0 <= nc && nc < M && grid[nr][nc] == 1) {
        grid[nr][nc] = 0;
        stack_push(&stack, (Point){nr, nc});
        count++;
      }
    }
  }

  return count;
}

static void test_dfs_iterative(void) {
  N = 3;
  M = 4;

  grid[0][0] = 1;
  grid[0][1] = 1;
  grid[1][1] = 1;
  grid[2][3] = 1;

  assert(dfs_iterative(0, 0) == 3);
  assert(grid[0][0] == 0);
  assert(grid[0][1] == 0);
  assert(grid[1][1] == 0);
  assert(grid[2][3] == 1);
  assert(dfs_iterative(2, 3) == 1);
}

int main(void) {
  Stack stack;
  Point popped = {-1, -1};

  stack_init(&stack);
  assert(stack_is_empty(&stack));
  assert(!stack_pop(&stack, &popped));
  assert_point(popped, -1, -1);

  stack_push(&stack, (Point){1, 1});
  stack_push(&stack, (Point){1, 2});
  stack_push(&stack, (Point){2, 2});

  assert(stack_pop(&stack, &popped));
  assert_point(popped, 2, 2);
  assert(stack_pop(&stack, &popped));
  assert_point(popped, 1, 2);
  assert(stack_pop(&stack, &popped));
  assert_point(popped, 1, 1);
  assert(stack_is_empty(&stack));

  test_dfs_iterative();

  puts("stack and iterative DFS tests passed");
  return 0;
}
