# Algorithm Repository Structure Design

## Goal

Reorganize every algorithm source file under a language-first layout so that
Python and C solutions are clearly separated while each language uses the
same topic vocabulary. Preserve source contents and Git history; this work is
a filesystem and repository-metadata reorganization, not a solution rewrite.

## Target layout

```text
solutions/
  python/
    bit/
    brute-force/
    divide-and-conquer/
    dynamic-programming/
    graph/
      dijkstra/
      mst/
    greedy/
    implementation/
      simulation/
    math/
    search/
    data-structures/
      list/
      stack/
      tree/
    string/
  c/
    array/
    math/
    search/
    simulation/
    string/
    data-structures/
      linked-list/
    misc/
  practice/
    c/
      structs/
```

`search` is the shared home for BFS and DFS work. `misc` is reserved for a
solution whose topic cannot be determined reliably from its current name or
code. It avoids inventing a wrong classification and should be emptied as
future classifications become clear.

## Migration rules

1. Every `.py` file moves below `solutions/python/`, except reusable study
   material that is explicitly language practice; none currently require that
   exception.
2. Every C problem solution moves below `solutions/c/`; the three `Struct_Ex`
   examples move to `practice/c/structs/`.
3. Existing topic names normalize to the target vocabulary:
   - `DFS, BFS` and C `BFS` become `search`.
   - `DynamicProgramming`, `DivideConquer`, and `DataStructure` become
     kebab-case target directories.
   - C `Array`, `math`, `Simulation`, and `String` become their lower-case
     equivalents.
4. Nested specializations remain nested: Python `Graph/Dijkstra` maps to
   `graph/dijkstra`, `Graph/MST` to `graph/mst`, and
   `Implementation/Simulation` to `implementation/simulation`.
5. The legacy Python groups `BOJ/IM`, `SWtest`, `Delta`, and `CodeTree` are
   classified by their existing subject where clear; otherwise they go to
   `implementation` rather than retaining a platform-specific top-level
   directory.
6. Problem-platform identifiers stay in filenames (`boj`, `swea`, `leet`,
   `atcoder`, and `codetree`), so the directory structure remains algorithm
   focused.
7. Incomplete files move with their corresponding topic. They are neither
   deleted nor edited as part of this reorganization.

## Repository metadata

- Add a root `README.md` explaining the layout, naming convention, and how to
  add a new solution.
- Add or update `.gitignore` to exclude IDE metadata and CMake build output
  (`.idea/`, `.vscode/`, `C/cmake-build-*/`, and common compiled artifacts).
- Remove the old empty category directories only after all source files have
  been moved.
- Replace the project-specific `C/CMakeLists.txt` with no build target during
  this migration. A single executable cannot contain every standalone problem
  file because they each define `main`; its removal avoids a misleading build
  entry point. The untracked file is not deleted without a separate explicit
  approval.

## Validation

1. Confirm that the pre- and post-migration counts match: 140 Python files and
   24 C files.
2. Confirm no source file remains in a legacy top-level source directory.
3. Use `git diff --summary` to ensure moves are recognized as renames where
   content is unchanged.
4. Verify no build directories or Python cache files are newly tracked.
