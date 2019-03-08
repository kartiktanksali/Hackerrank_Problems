#
#
#def merge_the_tools(string, k):
#    # your code goes here
#    sub = 0
#    lst = []
#    n = len(string)
#    sub = int(n/k)
#    for i in string:
#        for j in string:
#            if i!=j:
#                if len(lst)<sub:
#                    lst.append(i+j)
#                    
#    print(sub)
#    for i in lst:
#        print(i)
#
#
#if __name__ == '__main__':
#    string, k = input(), int(input())
#    merge_the_tools(string, k)
#    

#S, N = input(), int(input()) 
#for part in zip(*[iter(S)] * N):
#    d = dict()
#    print(part)
#    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

s = input()
k =int(input())
temp = []
len_temp = 0
for item in s:
    len_temp += 1
    if item not in temp:
        temp.append(item)
    if len_temp == k:
        print(''.join(temp))
        temp = []
        len_temp = 0