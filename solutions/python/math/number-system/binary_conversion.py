"""
0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어서, 10진수로 출력한다.
"""


def from_binary_to_decimal(arr):
    decimal = 0
    target_len = len(arr)
    for j in range(target_len):
        n = 0 if arr[j] == "0" else 1
        decimal += (2 ** (target_len - j)) * n

    return decimal


binary_nums = input()
d = len(binary_nums)

# 받아온 2진수 배열을 7개씩 끊어서 본다
# 0~6 / 7~13 / 14~20
decimal_nums = []
for i in range(0, d, 7):
    target_binary = binary_nums[i:i + 6]
    # print(target_binary)
    decimal_nums.append(from_binary_to_decimal(target_binary))

print(*decimal_nums)
