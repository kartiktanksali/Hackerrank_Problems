#Lists in python
dif_list = ["Kartik","Shruti",24,26,True,99.999]
str_list = ["Cats","Dogs","Lion","Tiger","Cheetah"]
int_list = [12,24,36,48,60,12,34,56]

#print(dif_list)
#print(str_list)
#print(int_list)
#
#print(dif_list[0])
#print(str_list[3])
#print(int_list[-5])

#for d in dif_list:
#    print(d)
#
#print("\n")
#
#for i in range(0,len(str_list)):
#    print(str_list[i])
#    
#dif_list.append("kartik")
#print(dif_list)
#
#
#str_list.extend(["Hyna","Turtle"])
#print(str_list)
#
#dif_list.insert(3,[17,18])
#print(dif_list)
#
#print(dif_list[3][0])
#
#int_list.sort()
#
#int_list.reverse()
#
#print(int_list)

#new_dif = dif_list
#print(new_dif)
#
#new_dif[0],new_dif[3] = new_dif[1],new_dif[2]
#
#print(new_dif)

#new_list = []
#
#for i in range(1,11):
#    new_list.append(i)
#    
#print(new_list)


#print(chr(90))

#A_Z_list = []
#
#for i in range(65,91):
#    A_Z_list.append(chr(i))
#    
#print(A_Z_list)


#print(chr(97))


#a_z_list = []
#for i in A_Z_list:
#    i = ord(i)+32
#    a_z_list.append(chr(i))
#print(a_z_list)



#a_z_list = [chr((ord(i)+32)) for i in A_Z_list]
#print(a_z_list)
    
#name_list = ["sejal","katlin","taylor"]
#
#print(name_list)
#
#new_name_list = [names.upper() for names in name_list]
#
#print(new_name_list)
#numbers = []
#for i in range(1,11):
#    numbers.append(i)
#print(numbers)
#
#odd_even = [num*2 if num%2==0 else num*3 for num in numbers]
#print(odd_even)
#
# 
#[odd_even.remove(num) for num in odd_even if num%3==0]
#print(odd_even)




#n = int(input())
#arr = list(map(int, input().split()))
#
##maximum=0
##for i in arr:
##    if i>maximum:
##        maximum = i
#
#arr.sort()
#
#def foo():
#    for i in arr:
#        for j in arr:
#            if i!=j:
#                runner_up = j
#    print(runner_up)
#    
#
#foo()
#
#

l = []
for _ in range(int(input())):
        row = []
        name= input()
        score = float(input())
        row.append(name)
        row.append(score)
        l.append(row)

#for i in range(0,len(l)):
#    print(l[i][1])

from operator import itemgetter
l = sorted(l,key=itemgetter(1))

minimum = l[0][1]

second_min=0
#for i in l:
#    for j in l:
#        if i!=j:
#            second_min = j
#            print(second_min)

#for i in range(len(l)):
#    if l[i][1] != l[i+1][1]:
#        second_min == l[i+1][1]

#for i in range(len(l)):
#    for j in range(len(l)):
#        if l[i][1] != l[j][1]:
#            second_min = l[j][1]
    
#for i in range(len(l)):
#    print(f"l[i][1] value is : {l[i][1]} and l[i+1][1] values is {l[i+1][1]}")
#    if l[i][1] != l[i+1][1]:
#        second_min = l[i+1][1]
print("\n")
print(minimum)
print("\n")
for i in l:
    if i[1] > minimum:
        second_min=i[1]
        break
    


print("\n")
print(second_min)

new_list = []
#for i in range(len(l)):
#    print(l[i])

for i in range(len(l)):
    if l[i][1] == second_min:
        new_list.append(l[i])

new_list = sorted(new_list,key=itemgetter(0))
for i in range(len(new_list)):
    print(new_list[i][0])









