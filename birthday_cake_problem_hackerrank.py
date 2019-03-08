
ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

#result = birthdayCakeCandles(ar)

#fptr.write(str(result) + '\n')

print(ar)

ar.sort()
ar.reverse()

maximum = ar[0]

print(maximum)

count = 0
for i in ar:
    if i == maximum:
        count = count+1

print(count)