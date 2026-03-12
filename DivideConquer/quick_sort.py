# ---------------------------------------------------------------------------------
# [Hoare]

def quick_sort(arr, start, end):
    if start >= end:
        # start = end => 정렬할 원소가 1개밖에 없다는 것을 의미
        # start > end => 빈 arr임을 의미
        # 해당 경우에는 종료
        return

    # 첫번째 원소를 pivot 으로 잡는다.
    pivot = start
    left = pivot + 1
    right = end

    while left <= right:

        # left 포인터는 pivot 보다 작은 값들은 그냥 지나친다
        # => left 는 pivot 보다 큰 값을 찾는 것이 목적이므로 그때 멈춘다.
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # right 포인터는 pivot 보다 큰 값들을 그냥 지나친다
        # => right 는 pivot 보다 작은 값을 찾는 것이 목적이기 때문에 그때 멈춘다.
        # right 포인터는 오른쪽에서 왼쪽에서 올 때, pivot 자리는 침범하지 않아야 한다.
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            # 왼쪽에서 출발한 left 포인터와 오른쪽에서 출발한 right 포인터가 엇갈린 상태이다
            # => 즉, pivot 이 들어갈 적절한 위치를 찾은 경우이기 때문에 right 위치에 pivot을 넣어준다.
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            # left <= right
            # 해당 경우는 left, right 포인터 모두 pivot 보다 크고 작은 값들, 즉 정렬이 필요한 값들을 찾은 경우이다.
            # => 따라서 left와 right의 위치 swap이 필요하다.
            arr[left], arr[right] = arr[right], arr[left]

    # 기준으로 잡은 pivot은 적절한 자리를 찾아 들어갔기 때문에
    # pivot을 기준으로 왼쪽 배열, 오른쪽 배열에 대한 정렬이 필요하다.
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, len(nums) - 1)

    print(f"#{test_case}", end=" ")
    print(*nums)


# ---------------------------------------------------------------------------------
# [Lomuto]


def partition_lomuto(arr, start, end):
    # 맨끝의 원소를 pivot으로 설정
    pivot = arr[end]
    # i는 현재 partition 구간에서 pivot보다 작은 값들의 마지막 idx를 의미한다.
    # 즉, 현재 정해놓은 start, end 구간에서 pivot 원소보다 작은 값들 중 마지막 idx를 의미하는 것
    # i 초기값을 그냥 -1로 해버리면 정해놓은 구간에서 정렬이 되는 것이 아니라 항상 전체 구간에 대해서 swap이 발생할 수 있다.
    # 왜냐하면 -1로 한다는 것의 의미는 현재 pivot보다 작은 값이 아직 존재하지 않는다는 것을 의미하기 때문이다.
    i = start - 1

    for j in range(start, end):
        # j 번째 숫자와 pivot 숫자를 비교하면서 진행한다.
        # => pivot보다 j번째 숫자가 작은 경우, i += 1 와 swap
        # => pivot보다 j번째 숫자가 큰 경우, 아무것도 하지 않는다.
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 반복문이 끝났을 때의 i + 1 번째가 바로 pivot이 들어갈 위치이다.
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort_lomuto(arr, start, end):
    if start >= end:
        return

    pivot_idx = partition_lomuto(arr, start, end)
    quick_sort_lomuto(arr, start, pivot_idx - 1)
    quick_sort_lomuto(arr, pivot_idx + 1, end)


T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    quick_sort_lomuto(nums, 0, len(nums) - 1)

    print(f"#{test_case}", end=" ")
    print(*nums)
