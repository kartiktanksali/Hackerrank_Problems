#word_order
#n = int(input())
#words = []
#
#for i in range(n):
#    word = input()
#    words.append(word)
#
#s = set(words)
#print(len(s))
#
#temp = words
#occurence_list= []
#
#for i in temp:
#    count = 0
#    count = temp.count(i)
#    occurence_list.append(count)
#    if count > 1:
#        temp.remove(i)
#
#for i in occurence_list:
#    print(i, sep=' ' , end = ' ')

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
    