N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

end_h = 0
meeting_cnt = 0

for start, end in meetings:
    if end_h <= start:
        end_h = end
        meeting_cnt += 1

print(meeting_cnt)
