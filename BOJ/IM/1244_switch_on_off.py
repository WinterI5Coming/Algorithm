n = int(input()) # 스위치 개수 = 100이하의 양의 정수
switch_list = list(map(int,input().split())) # 스위치 리스트
stu_n = int(input()) # 학생 수 = 100이하의 양의 정수
stu_list = [list(map(int,input().split())) for _ in range(stu_n)] # 학생 리스트 [성별(1 남, 2 여), 받은 수]

# 학생 리스트를 순회하면서 스위치를 작동시킨다
# 남학생 => 받은 숫자의 배수 스위치 작동
# 여학생 => 받은 숫자를 기준으로 대칭이 될 수 있게 스위치 작동 (단, 스위치 상태도 대칭이 되어야 한다)
# 출력은 한 줄에 20개까지만 출력

for gender, s_num in stu_list:
    s_idx = s_num - 1

    if gender == 1:
        # 남학생의 경우
        for m in range(s_idx, n, s_num):
            switch_list[m] = 1 if switch_list[m] == 0 else 0

    else:
        # 여학생의 경우
        # 대칭을 위해 얼만큼의 칸이 필요한지를 먼저 구한다
        symmetry_n = s_idx if s_idx < (n-1) - s_idx else (n-1) - s_idx
        switch_list[s_idx] = 1 if switch_list[s_idx] == 0 else 0
        for w in range(1, symmetry_n + 1):
            if switch_list[s_idx - w] != switch_list[s_idx + w]:
                break
            switch_list[s_idx - w] = switch_list[s_idx + w] = 1 if switch_list[s_idx - w] == 0 else 0

if len(switch_list) <= 20:
    print(*switch_list)
else:
    for i in range(len(switch_list)):
        if i != 0 and i % 20 == 0:
            print()
        print(switch_list[i], end=" ")
