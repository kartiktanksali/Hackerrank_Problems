#Company_logo hackerrank
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

s = OrderedCounter(sorted(input()))
for i in s.most_common(3):
    print(*i)
   

#s = sorted(input())
#print(s)
#
#s = OrderedCounter(s)
#print(s)
#
#l = s.most_common(4)
#print(l)