#Python Dicktionaries
car_dict = {"company":"Ford","name":"Aspire","make":2017,"miles":22000,"running":True}

#print(car_dict)
#print("\n")
#print(car_dict["make"])
#print("\n")
#
#for v in car_dict.values():
#    print(v)
#
#print("\n")
#
#for k in car_dict.keys():
#    print(k)
#    
#print("\n")
#
#for k,v in car_dict.items():
#    print(f"The keys are {k} and their values {v}")
#    
#clone = car_dict
#
#clonecopy = car_dict.copy()
#
#d = {}.fromkeys(["name","age"],"unknwon")
#
#print(d)
#
#a = car_dict.get("name")
#print(a) 

#playlist = {"title":"Travelling Songs", "author":"Kartik Tanksali",
#            "songs":[{"title":"Lambergini","artist":["Melvin","Harleen"],"duration":3.40},
#                     {"title":"Anjana Anjani","artist":["Amit","Shreya"],"duration":4.45},
#                     {"title":"Channa Mereya","artist":["Arijit"],"duration":4.32}
#            ]}
#sums=0
#for i in playlist["songs"]:
#    print(i["duration"])
#    sums = sums + i["duration"]
#print("Sum = ",sums)

#numbers = {"one":1,"two":2,"three":3,"four":4}
#
#square_numbers = {key: value**2 for key,value in numbers.items()}
#
#print(square_numbers)

#names = {"appa":"shreekant","amma":"kalpana","dummi":"shruti"}
#
#upper_name = {key.upper():value.upper() for key,value in names.items() }
#
#print(upper_name)


#nums = [1,2,3,4,5]
#
#even_odd = {num : ("even" if num%2==0 else "odd") for num in nums}
#
#print(even_odd)

#Hackerrank


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores    
query_name = input()
average = 0
sum=0
for i in student_marks[query_name]:
    sum += i
average=sum/3
print(round(average,2))
