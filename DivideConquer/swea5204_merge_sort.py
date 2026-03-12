def merge_sort(arr):
    if len(arr) == 1:
        return arr

    # 분할한다.
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # 분할한 것들을 정렬해야 한다.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    global count

    if left[-1] > right[-1]:
        count += 1

    merged_arr = []
    l_idx, r_idx = 0, 0
    # left 와 right 를 오름차순으로 정렬한다.
    # => 한 쪽이 다 없어질 때 까지
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            merged_arr.append(left[l_idx])
            l_idx += 1
        else:
            merged_arr.append(right[r_idx])
            r_idx += 1

    # 남아있는 것들을 merged_arr 에 이어준다.
    merged_arr.extend(left[l_idx:])
    merged_arr.extend(right[r_idx:])

    return merged_arr


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    count = 0
    sorted_nums = merge_sort(nums)

    print(f"#{test_case} {sorted_nums[N // 2]} {count}")
