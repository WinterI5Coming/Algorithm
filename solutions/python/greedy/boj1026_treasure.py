"""
길이가 N인 정부 배열 A, B가 있다.
함수 S를 다음과 같이 정의한다. => S = A[0] * B[0] + ... + A[N-1] * B[N-1]

S의 값을 가장 작게 만들기 위해 배열 A를 재배열 하자. 단, B는 재배열 불가.
"""

from collections import deque

N = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort(reverse=True)
b_order = sorted([(list_b[i], i) for i in range(N)], key=lambda x: x[0])
# print(b_order)

S = 0
for i, b_el in enumerate(b_order):
    # print(i, b_el)
    S += list_a[i] * b_el[0]

print(S)
