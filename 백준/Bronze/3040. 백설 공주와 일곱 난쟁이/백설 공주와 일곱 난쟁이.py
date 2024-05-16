from itertools import combinations

arr = [0]*9

for i in range(9):
    arr[i] = int(input())

for i in combinations(arr, 7):
    if sum(i) == 100:
        res = i

for i in range(7):
    print(res[i])