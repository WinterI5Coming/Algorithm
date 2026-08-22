# Algorithm Study

Algorithm problem solutions organized by language and topic.

## Layout

- `solutions/python/<topic>/`: Python problem solutions.
- `solutions/c/<topic>/`: C problem solutions.
- `practice/c/structs/`: C language and structure exercises.

Topics use lowercase kebab-case names. `search` contains BFS and DFS work.
Existing platform identifiers remain in filenames when present.

## Adding a solution

1. Choose the language directory.
2. Choose the algorithm-topic directory.
3. Prefer a platform-and-problem filename such as `boj1234_example.py`.
4. Do not commit IDE or compiler-generated files.

## CLion

Open the repository root in CLion, then reload the CMake project. Each
configured C source appears as a separate run target, so select the problem
name from the top-right run configuration menu and run it independently.

Function-only LeetCode files and unfinished exercises are intentionally not
configured as executable targets.

## Commit convention

```text
solve: BOJ 2178 maze search
fix: BOJ 14502 resolve timeout
refactor: organize shared BFS logic
docs: add BFS study note
```
