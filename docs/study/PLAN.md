# 학습 계획

**2026-08-23 전면 개정.** 초안(8/23 오전)은 `algo-study` 임시 워크스페이스에서 이 저장소를 모르는 상태로 작성했다. 기존 자산 121개 Python 풀이 + 19개 C 풀이를 확인한 뒤 근본적으로 다시 세웠다. → [[0004-existing-assets-change-the-plan]]

## 계획을 지배하는 판단

**① C 문법이 병목이고 알고리즘 개념은 살아있다.** 2178 세션에서 막힌 9번이 전부 C 규칙이었다 ([[0001-python-to-c-state-handling]]).

**② 초안의 1·2단계 문제 목록이 이미 Python으로 풀려 있다.** `solutions/python/search/`(38개)에 2178, 2667, 1697, 7576, 1926이 전부 있고, 그보다 훨씬 어려운 것도 있다 — 2206/14442 벽 부수고 이동(상태 차원 추가), 13549 숨바꼭질3(0-1 BFS), 13913(경로 복원), 1600 원숭이, 7569 3차원 토마토, 2573 빙산, 2146 다리 만들기.

**③ 그래서 학습 방식이 바뀐다.** 새 문제를 찾는 대신 **이미 Python으로 푼 문제를 C로 재구현**한다. 이유:
- 알고리즘을 다시 고민할 필요가 없어 **C 구현에 100% 집중**된다
- 막히면 **본인이 예전에 쓴 Python 코드**와 대조할 수 있다. 남의 해설보다 훨씬 낫다
- 정답을 이미 알고 있으니 검증이 쉽다

**④ 난이도를 올려야 한다.** 초안에 넣은 2606 바이러스 같은 문제는 이 사람에게 너무 쉽다.

## 단계

### 1단계 · 격자 탐색 C 재구현 (1주) — 진행 중
- ✅ 큐 (전역 배열 방식) — `boj2178_maze_search.c`
- ✅ 연결 요소 / 다중 호출 BFS — `boj2667_apartment_complexes.c`
- **스택 (구조체+포인터 방식)** → 반복 DFS. 큐(전역)와 대조 학습 ([[0003-globals-vs-struct-encapsulation]]). 비교 코드: `practice/c/structs/queue_two_designs.c`
- 재구현 대상: `boj7576_tomato`(다중 시작점) → `boj2206_breaking_wall_and_move`(**상태 차원 추가 — visited가 3차원이 되는 이유**) → `boj13913`(경로 복원)
- **목표: 격자 BFS/DFS를 C로 30분 안에 자동 작성**

### 1.5단계 · 연결 리스트 — 대부분 완료, 점검만 (0.5주)
이미 있음: `solutions/c/data-structures/linked-list/linked_list.c`, `double_linked_list.c`, `practice/c/structs/struct_single_linked_list.c`

- 남은 것: `malloc`/`free` 수명 관리와 메모리 누수 점검, 불투명 포인터 패턴, Floyd 순환 탐지
- **`malloc`이 정답인 경우**를 확인하는 자리 — 1단계에서 "정적 배열이 낫다"만 배운 상태를 방치하면 "malloc은 나쁘다"로 굳는다 ([[0002-coding-test-bias-in-curriculum]])

### 2단계 · 시뮬레이션 C 재구현 (2주) ← 삼성 A형 핵심
- 2차원 배열 회전·이동·충돌, 구조체 배열 정렬
- 재구현 대상: `boj14500_tetromino` / `boj14891_gear` / `implementation/simulation/` 하위 / SWEA 기출
- 미완성 정리: `solutions/c/simulation/swea2383_lunch_time.c`, `solutions/c/search/2025_kakao_prevent-spoiler.c`
- 알고리즘 난이도는 낮고 **구현 정확도가 전부**

### 3단계 · 자료구조 직접 구현 (2주) ← 미션의 "라이브러리 없이" 목표 핵심
C에 아직 **없는** 것들. 여기가 진짜 새 학습이다.
- **힙** → 우선순위 큐 → 다익스트라 (`solutions/python/graph/` 참고)
- **해시맵** (체이닝)
- `qsort`와 비교 함수 (2667에서 이미 사용 ✅)
- 그래프 인접 리스트 (연결 리스트 지식 활용)

### 4단계 · 트리 (1주)
- 트리의 C 표현 3가지: 배열 인덱스 / 인접 리스트 / 포인터 노드
- 순회, 깊이. 재귀 깊이와 스택 오버플로 실측

### 5단계 · DP·그리디·완전탐색 C 재구현 (3주)
Python에는 있으나 C에는 전무한 영역.
- `dynamic-programming`(6) / `greedy`(12) / `brute-force`(13) / `divide-and-conquer`(7) / `bit`(2)
- C 문법 부담이 적어 순수 사고 훈련. 비트마스크는 C가 오히려 자연스럽다

## 매 세션 공통

- **문제 전 복잡도 계산** — `docs/study/reference/complexity-budget.html` 체크리스트
- **복습: +3 / +7 / +21일** — 반드시 **빈 파일에서 재구현**. 예전 코드를 보는 건 재인(再認)이지 기억이 아니다
- **패턴 3개 이상이면 세션 내 인터리빙** — 미션의 "30초 분류" 목표
- **`docs/study/reference/` 축적** — 최종 산출물. 스택·힙 구현 후 **"C 코테 자료구조 관용구"** 치트시트 (큐/스택/힙 골격, 선언 순서, scanf 포맷, 연쇄 비교 등 함정)
- **저장소 규칙 준수** — `solutions/c/<topic>/`, `CMakeLists.txt` 등록, `tests/<target>/`, 커밋 컨벤션. `README.md` 참조

## 미확정 / 조정 트리거

- **Python 재구현 방식의 효과를 1단계에서 검증한다.** 정답을 아는 상태가 오히려 사고를 건너뛰게 만든다면, 신규 문제와 섞는다
- 목표 시점(기업 코테 일정)이 정해지면 2단계를 앞으로 당긴다
- 개발 환경은 **CLion + CMake**가 주력. `algo-study`에서 만든 VS Code 설정(`launch.json`, `tasks.json`)은 이 저장소에 옮기지 않았다
- 미션이 바뀌면 계획을 다시 짜고 학습 기록을 남긴다
