from itertools import combinations
n, m=map(int, input().split())

nums=[x+1 for x in range(n)]
answer=combinations(nums, m)

for idx, arr in enumerate(answer) :
    print(*arr)