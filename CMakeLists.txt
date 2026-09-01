cmake_minimum_required(VERSION 3.20)

project(algorithm_study LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

function(add_solution target source)
    add_executable(${target} ${source})
endfunction()

# Array
add_solution(boj11098_help_chelsea solutions/c/array/boj11098_help_chelsea.c)

# Data structures
add_solution(double_linked_list solutions/c/data-structures/linked-list/double_linked_list.c)
add_solution(linked_list solutions/c/data-structures/linked-list/linked_list.c)
add_solution(swea13501_edit_num_array solutions/c/data-structures/linked-list/swea13501_edit_num_array.c)
add_solution(swea_secret_code3 solutions/c/data-structures/linked-list/swea_secret_code3.c)

# Math
add_solution(boj10984_get_my_grade solutions/c/math/boj10984_get_my_grade.c)
add_solution(boj1408_24 solutions/c/math/boj1408_24.c)
add_solution(boj1977_perfect_square solutions/c/math/boj1977_perfect_square.c)
add_solution(boj2609_gcd_lcm solutions/c/math/boj2609_gcd_lcm.c)

# Miscellaneous and search
add_solution(atcoder_cookies solutions/c/misc/atcoder_cookies.c)
add_solution(boj2178_maze_search solutions/c/search/boj2178_maze_search.c)
add_solution(boj2667_apartment_complexes solutions/c/search/boj2667_apartment_complexes.c)
add_solution(swea5653_cell solutions/c/search/swea5653_cell.c)

# String
add_solution(boj10809_find_alphabet solutions/c/string/boj10809_find_alphabet.c)
add_solution(boj1152_cnt_of_word solutions/c/string/boj1152_cnt_of_word.c)
add_solution(boj2675_repeat_str solutions/c/string/boj2675_repeat_str.c)

# C language practice
add_solution(queue_two_designs practice/c/structs/queue_two_designs.c)
add_solution(stack_iterative_dfs practice/c/structs/stack_iterative_dfs.c)
add_solution(struct_point practice/c/structs/struct_point.c)

# Files intentionally omitted:
# - LeetCode functions without main()
# - unfinished problem solutions
# - incomplete C practice examples
