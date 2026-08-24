# 학습 워크스페이스

알고리즘 공부의 **상태**가 여기에 있다. 문제 풀이 코드는 `solutions/`, 공부 계획과 기록은 여기.

## 다음 세션 시작하는 법

이 저장소 루트에서 Claude Code를 실행한 뒤 `/study` 입력.

```
cd C:\Users\Winter\Desktop\Study\Algorithm
claude
```
그리고 `/study`

`/study`가 자동으로 하는 일:
1. `MISSION.md`(왜 공부하는가) → `PLAN.md`(단계별 계획) → `NOTES.md`(선호·교육 방침) 읽기
2. 최근 `learning-records/` 읽어서 어디까지 했는지 파악
3. `solutions/`와 `git log` 확인 — 이미 푼 걸 또 가르치지 않기 위해
4. 복습 예정일이 지난 문제 확인
5. 세션 계획 제안 (복습 1개 + 새 항목 1~2개)

특정 주제를 하고 싶으면 `/study 스택 구현` 처럼 인자를 붙이면 된다.

## 파일 지도

| 파일 | 역할 |
|---|---|
| `MISSION.md` | 왜 공부하는가. 모든 교육 결정의 기준 |
| `PLAN.md` | 5단계 커리큘럼. 근거가 바뀌면 개정하고 학습 기록을 남긴다 |
| `NOTES.md` | 선호(언어·페이스)와 교육 방침 결정 사항 |
| `RESOURCES.md` | 외부 자료 링크 |
| `learning-records/000N-*.md` | 비자명한 통찰. 번호순. 다음에 뭘 가르칠지 계산하는 근거 |
| `learning-records/<문제>-notes.md` | 문제별 기록: 접근법, 복잡도, 막힌 지점, 복습 예정일 |
| `reference/*.html` | 치트시트. 계속 들춰보는 문서 |
| `problems/*-statement.md` | 문제 설명 보관 |

## 현재 진행 상황 (2026-08-24 기준)

**1단계 · 격자 탐색 C 재구현** 진행 중

- ✅ `boj2178_maze_search` — 큐(전역 배열), 격자 BFS 최단거리
- ✅ `boj2667_apartment_complexes` — 연결 요소, 다중 호출 BFS, `qsort`
- ⬜ **다음: 스택을 구조체+포인터 방식으로 구현** → 반복 DFS
  - 큐를 전역으로 만들었으니 대조 학습이 된다. 비교 코드: `practice/c/structs/queue_two_designs.c`
- ⬜ 그 다음: `boj7576_tomato`(다중 시작점) → `boj2206`(상태 차원 추가) → `boj13913`(경로 복원) C 재구현

**복습 예정: 2026-08-26** — 2178과 2667을 **빈 파일에서** 다시 작성.
확인 포인트: `pop()` 누락, `head`/`tail` 리셋, 연쇄 비교(`0 <= x < N` 금지), 배열 크기 상한.

## 학습 방식

**이미 Python으로 푼 문제를 C로 재구현한다.** `solutions/python/`에 121개가 있고, 알고리즘 개념은 살아있으나 C 구현이 병목이기 때문. 막히면 본인이 예전에 쓴 Python 코드와 대조할 수 있다. 자세한 근거는 `learning-records/0004-existing-assets-change-the-plan.md`.

## 저장소 규칙 (풀이를 추가할 때)

1. `solutions/c/<topic>/<platform><번호>_<snake_case>.c`
2. `CMakeLists.txt`에 `add_solution(<타겟> <경로>)` 등록 — 안 하면 CLion에서 안 보인다
3. 테스트 입력은 `tests/<타겟>/input-<케이스>.txt`
4. 커밋: `solve: BOJ 2178 maze search` 형식
