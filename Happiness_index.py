#Happiness Index
n, m = input().split()

arr = input().split()
A = set(input().split())
B = set(input().split())

arr = list(map(int, arr))
A = set(map(int,A))
B = set(map(int,B))

happiness_index = 0

for i in arr:
    if i in A:
        happiness_index += 1
    if i in B:
        happiness_index -= 1

print(happiness_index)