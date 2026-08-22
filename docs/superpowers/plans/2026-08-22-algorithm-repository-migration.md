# Algorithm Repository Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move every algorithm source into a language-first directory hierarchy while preserving source contents and Git rename history.

**Architecture:** `solutions/python` and `solutions/c` share normalized algorithm-topic names. C language exercises live in `practice/c/structs`. Existing solution contents remain unchanged; only paths, documentation, and ignore rules change.

**Tech Stack:** Git, PowerShell, GCC C11 syntax checks, Python standard-library compilation.

**Spec:** `docs/superpowers/specs/2026-08-22-algorithm-repository-structure-design.md`

## Global Constraints

- Preserve all 140 Python files and 24 C files; do not delete or rewrite solution code.
- Use `git mv` for tracked files. Use `Move-Item` only for source files that are already untracked.
- Preserve filenames exactly as they are.
- Move incomplete files too, but do not repair them as part of this migration.
- Do not delete the untracked `C/CMakeLists.txt`.
- Ignore IDE metadata, CMake output, Python bytecode, and compiled binaries.

---

### Task 1: Document and protect the target layout

**Files:**

- Create: `README.md`
- Create or modify: `.gitignore`

**Interfaces:**

- Consumes: the target layout in the approved design specification.
- Produces: the navigation and ignore rules used by all migrated sources.

- [ ] **Step 1: Record the source inventory**

Run:

```powershell
$pythonCount = (rg --files -g '*.py' -g '!C/cmake-build-debug/**' | Measure-Object).Count
$cCount = (rg --files -g '*.c' -g '!C/cmake-build-debug/**' | Measure-Object).Count
"Python=$pythonCount C=$cCount"
```

Expected: `Python=140 C=24`.

- [ ] **Step 2: Add repository guidance**

Create `README.md` with these sections:

```markdown
# Algorithm Study

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
```

- [ ] **Step 3: Add ignore rules**

Ensure `.gitignore` contains:

```gitignore
.idea/
.vscode/
C/cmake-build-*/
__pycache__/
*.py[cod]
*.exe
*.out
*.o
*.obj
```

- [ ] **Step 4: Verify metadata**

Run:

```powershell
git diff --check -- README.md .gitignore
git check-ignore -v C/cmake-build-debug/ __pycache__/example.pyc
```

Expected: no whitespace errors and both generated-path examples are ignored.

- [ ] **Step 5: Commit metadata**

```powershell
git add README.md .gitignore
git commit -m "docs: document language-first solution layout"
```

### Task 2: Migrate Python sources by normalized topic

**Files:**

- Move: `Bit/*.py` → `solutions/python/bit/`
- Move: `BruteForce/*.py` → `solutions/python/brute-force/`
- Move: `DFS, BFS/*.py` → `solutions/python/search/`
- Move: `DivideConquer/*.py` → `solutions/python/divide-and-conquer/`
- Move: `DynamicProgramming/*.py` → `solutions/python/dynamic-programming/`
- Move: `Graph/Dijkstra/*.py` → `solutions/python/graph/dijkstra/`
- Move: `Graph/MST/*.py` → `solutions/python/graph/mst/`
- Move: `Graph/*.py` → `solutions/python/graph/`
- Move: `Greedy/*.py` and `CodingTestBook/Greedy/*.py` → `solutions/python/greedy/`
- Move: `Implementation/Simulation/*.py` → `solutions/python/implementation/simulation/`
- Move: `Implementation/*.py`, `BOJ/IM/*.py`, and `SWtest/{A,IM}/*.py` → `solutions/python/implementation/`
- Move: `List/*.py`, `Stack/*.py`, and `Tree/*.py` → matching `solutions/python/data-structures/{list,stack,tree}/`
- Move: `String/*.py` → `solutions/python/string/`
- Move: `NumberSystem/*.py` → `solutions/python/math/number-system/`
- Move: `CodeTree/codetree_card_shuffle.py` → `solutions/python/data-structures/list/`
- Move: `Delta/1954_snail.py`, `Delta/9490_ballon.py`, and `Delta/code_tree_ruin_exploration.py` → `solutions/python/implementation/simulation/`
- Move: `Delta/code_tree_1or3_bfs.py` and `Delta/code_tree_1or3_dfs.py` → `solutions/python/search/`
- Move: `Delta/code_tree_patrol_order.py` → `solutions/python/graph/`

**Interfaces:**

- Consumes: the topic vocabulary from Task 1.
- Produces: 140 Python sources under `solutions/python/`.

- [ ] **Step 1: Create all Python destination directories**

Run:

```powershell
$dirs = @(
  'solutions/python/bit',
  'solutions/python/brute-force',
  'solutions/python/search',
  'solutions/python/divide-and-conquer',
  'solutions/python/dynamic-programming',
  'solutions/python/graph/dijkstra',
  'solutions/python/graph/mst',
  'solutions/python/greedy',
  'solutions/python/implementation/simulation',
  'solutions/python/data-structures/list',
  'solutions/python/data-structures/stack',
  'solutions/python/data-structures/tree',
  'solutions/python/string',
  'solutions/python/math/number-system'
)
New-Item -ItemType Directory -Force -Path $dirs
```

- [ ] **Step 2: Rename tracked Python files**

Use `git mv` for every tracked path in this task's Files list. Move the currently untracked `DFS, BFS/swea1953_arrest_of_escaped_convict.py` with:

```powershell
Move-Item 'DFS, BFS/swea1953_arrest_of_escaped_convict.py' 'solutions/python/search/'
```

If a destination filename already exists, stop and report both source paths; do not overwrite either file.

- [ ] **Step 3: Validate Python preservation**

Run:

```powershell
$pythonCount = (rg --files solutions/python -g '*.py' | Measure-Object).Count
if ($pythonCount -ne 140) { throw "Expected 140 Python files, got $pythonCount" }
python -m compileall -q solutions/python
git diff --summary
```

Expected: 140 Python files, successful compilation, and tracked source changes reported as renames. Remove generated `__pycache__` folders before staging.

- [ ] **Step 4: Commit Python moves**

```powershell
git add -A solutions/python
git commit -m "refactor: organize Python solutions by topic"
```

### Task 3: Migrate C solutions and practice examples

**Files:**

- Move: `C/Array/*.c` → `solutions/c/array/`
- Move: `C/BFS/*.c` → `solutions/c/search/`
- Move: `C/DataStructure/LinkedList/*.c` and `C/DataStructure/LinkedList/swea13072_manage_soldier/*.c` → `solutions/c/data-structures/linked-list/`
- Move: `C/math/*.c` → `solutions/c/math/`
- Move: `C/Simulation/*.c` → `solutions/c/simulation/`
- Move: `C/String/*.c` → `solutions/c/string/`
- Move: `C/atcoder_cookies.c` → `solutions/c/misc/`
- Move: `C/Struct_Ex/*.c` → `practice/c/structs/`

**Interfaces:**

- Consumes: the target C categories in the design specification.
- Produces: all 24 C sources under `solutions/c/` or `practice/c/`.

- [ ] **Step 1: Create C destination directories**

Run:

```powershell
$dirs = @(
  'solutions/c/array',
  'solutions/c/search',
  'solutions/c/data-structures/linked-list',
  'solutions/c/math',
  'solutions/c/simulation',
  'solutions/c/string',
  'solutions/c/misc',
  'practice/c/structs'
)
New-Item -ItemType Directory -Force -Path $dirs
```

- [ ] **Step 2: Rename tracked C files**

Use `git mv` for every tracked source in this task's Files list. Do not move `C/CMakeLists.txt` or files below `C/cmake-build-debug/`.

- [ ] **Step 3: Move untracked C sources**

Run:

```powershell
Move-Item 'C/BFS/2025_kakao_prevent-spoiler.c' 'solutions/c/search/'
Move-Item 'C/DataStructure/LinkedList/swea13072_manage_soldier' 'solutions/c/data-structures/linked-list/'
Move-Item 'C/Simulation/swea2383_lunch_time.c' 'solutions/c/simulation/'
Move-Item 'C/Struct_Ex/struct_single_linked_list.c' 'practice/c/structs/'
Move-Item 'C/Struct_Ex/struct_student.c' 'practice/c/structs/'
```

- [ ] **Step 4: Validate C preservation**

Run:

```powershell
$cCount = (rg --files solutions/c practice/c -g '*.c' | Measure-Object).Count
if ($cCount -ne 24) { throw "Expected 24 C files, got $cCount" }
gcc -std=c11 -Wall -Wextra -fsyntax-only solutions/c/array/leet1_two_sum.c
gcc -std=c11 -Wall -Wextra -fsyntax-only solutions/c/search/swea5653_cell.c
gcc -std=c11 -Wall -Wextra -fsyntax-only solutions/c/data-structures/linked-list/swea13501_edit_num_array.c
gcc -std=c11 -Wall -Wextra -fsyntax-only practice/c/structs/struct_point.c
git diff --summary
```

Expected: 24 C files, the four complete samples pass syntax checks, and source content is unchanged.

- [ ] **Step 5: Commit C moves**

```powershell
git add -A solutions/c practice/c
git commit -m "refactor: organize C solutions by topic"
```

### Task 4: Complete the repository-wide validation

**Files:**

- Modify: `README.md` only if validation finds a documented path mismatch.

**Interfaces:**

- Consumes: all paths created by Tasks 1 through 3.
- Produces: a verified language-first source tree.

- [ ] **Step 1: Confirm legacy source directories are gone**

Run:

```powershell
$legacy = @('Bit','BOJ','BruteForce','CodeTree','CodingTestBook','Delta','DFS, BFS','DivideConquer','DynamicProgramming','Graph','Greedy','Implementation','List','NumberSystem','Stack','String','SWtest','Tree','C/Array','C/BFS','C/DataStructure','C/math','C/Simulation','C/String','C/Struct_Ex')
$legacy | Where-Object { Test-Path $_ }
```

Expected: no output. The top-level `C` directory may remain because the untracked CMake file and ignored build output were explicitly preserved.

- [ ] **Step 2: Run final inventory checks**

Run:

```powershell
$pythonCount = (rg --files solutions/python -g '*.py' | Measure-Object).Count
$cCount = (rg --files solutions/c practice/c -g '*.c' | Measure-Object).Count
"Python=$pythonCount C=$cCount"
git diff --check HEAD
git status --short
```

Expected: `Python=140 C=24`, no whitespace errors, and no generated artifact staged.

- [ ] **Step 3: Commit a documentation correction only when needed**

If Task 4 changed `README.md`, run:

```powershell
git add README.md
git commit -m "docs: finalize repository organization guide"
```

Otherwise do not create an empty commit.
