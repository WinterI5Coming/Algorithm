arr = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]

# 원소의 합이 10인 부분집합을 구한다
# visited = [False] * 10
stack = [([], arr)]

while stack:
    selected, remain  = stack.pop()

    if sum(selected) != 10:
        for i in range(len(remain)):

            n_remain = remain[i + 1:]
            stack.append((selected + [remain[i]], n_remain))

    else:
        print(*selected)
