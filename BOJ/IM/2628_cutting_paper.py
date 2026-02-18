n, m = map(int, input().split()) # 가로 길이 n, 세로 길이 m
cut_n = int(input())

cut_x = [0, m] # 세로를 자르는 것
cut_y = [0, n] # 가로를 자르는 것

for _ in range(cut_n):
    w, w_n = map(int, input().split())

    if w == 0:
        cut_x.append(w_n)

    else:
        cut_y.append(w_n)
cut_x.sort()
cut_y.sort()

max_w = 0
max_h = 0
for i in range(len(cut_x) - 1):
    max_w = max(max_w, cut_x[i + 1] - cut_x[i])

for j in range(len(cut_y) - 1):
    max_h = max(max_h, cut_y[j + 1] - cut_y[j])

# print(cut_x)
# print(cut_y)
# print(max_w, max_h)
print(max_w * max_h)