T = int(input())


# Hoare
def quick_sort_hoare(arr, start, end):
    if start >= end:
        return

    # 맨 앞의 원소를 pivot 으로 설정
    pivot = start
    left = start + 1
    right = end

    # left, right 두 포인터가 교차할때 까지 진행
    while left <= right:

        # left 포인터는 pivot 보다 큰 값을 찾는 것이 목적
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # right 포인터는 pivot 보다 작은 값을 찾는 것이 목적
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            # 두 포인터가 교차한 경우, pivot 원소를 right 위치로 이동한다.
            # => right 를 기준으로 왼쪽으로는 pivot 보다 작은 값, 오른쪽으로는 pivot 보다 큰 값으로 정렬되었기 때문이다.
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:
            # left <= right
            # 해당 경우는 left는 pivot보다 큰 값을 찾고, right는 pivot보다 작은 값을 찾은 경우이다.
            # 찾은 값을 서로 swap
            arr[left], arr[right] = arr[right], arr[left]

    # pivot의 위치가 확정된 경우 pivot을 기준으로 왼쪽과 오른쪽에 대한 정렬 진행
    quick_sort_hoare(arr, start, right - 1)
    quick_sort_hoare(arr, right + 1, end)


# Lomuto
def quick_sort_lomuto(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        # j 번재 숫자와 pivot을 비교한다.
        # => j 번째 숫자가 더 큰 경우에는 => 아무것도 하지 않는다.
        # => j 번째 숫자가 더 작은 경우 => i(경계) 증가 + swap
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 반복문이 끝난 경우, i+1 위치가 pivot이 들어갈 위치이다.
    # i+1을 기준으로 왼쪽이 pivot보다 작은 숫자들, 오른쪽이 pivot보다 큰 숫자들이기 때문
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    # i + 1을 기준으로 왼쪽, 오른쪽 정렬 진행
    quick_sort_lomuto(arr, start, i)
    quick_sort_lomuto(arr, i + 2, end)


for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # quick_sort_hoare(nums, 0, N - 1)
    quick_sort_lomuto(nums, 0, N - 1)

    print(f"#{test_case} {nums[N // 2]}")
