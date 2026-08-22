n = int(input()) # 30,000이하의 양의 정수

best_list = []

for i in range(n, -1, -1):
    list_ = [n, i]
    while True:
        nxt = list_[-2] - list_[-1]
        if nxt < 0:
            break
        list_.append(nxt)

    if len(list_) > len(best_list):
        best_list = list_

print(len(best_list))
print(*best_list)