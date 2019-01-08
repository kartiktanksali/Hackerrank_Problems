#Sets and tuples

l = []
for i in range(65,65+26):
    l.extend(chr(i))
#    
#l = tuple(l)
#
##print(l)
##
##print("\n")
##
##print(l.index("V"))
#
#car_dict = {"company":"Ford","name":"Aspire","make":2017,"miles":22000,"running":True}
#
#
#
#print(car_dict.items())
#

s = {1,2,3}
print(s)

v = {3,2,4}
print(v)
print(s|v)
print(s&v)  