#Looping
#li = [10,20,30,40]
#sum=0
#for c in li:
#    print('c' *10)

#for i in range(1,10):
#    if(i%2==0):
#        print(i)

#string = "Clean the room"
#
#number = input("How many times do I have to tell you this?")
#n = int(number)
#
#for i in range(1,n+1):
#    print("Time ",i,string)

#for i in range(1,21):
#    if i==4 or i==13:
#        print(i," Is an unlucky number")
#    elif i%2==0 and i!=4 and i!=13:
#        print(i, " Is an even number")
#    else:
#        print(i," Is an odd number")


#i=1
#while i<=20:
#    if i==4 or i==13:
#        print(i," Is an unlucky number")
#    elif i%2==0 and i!=4 and i!=13:
#        print(i, " Is an even number")
#    else:
#        print(i," Is an odd number")
#    i += 1


#for i in range(0,10):
#    print("\U0001f600"*i)
#    
#print("\n Using While")
#
#i=1
#while i<=10:
#    print("\U0001f600"*i)
#    i += 1

#for i in range(0,10):
#    for j in range(i,i+1):
#        print("\U0001f600"*i)


#i
#print(i)
#print(i,i+1)
#print(i,i+1,i+2)

#for i in range(1,12):
#    print("\n")
#    for j in range(1,i):
#        print(j,end='')

#for i in range(1,11,2):
#   print("*"*i)
#   
#
#        
#print(" "*5,"*"*1)
#print(" "*4,"*"*3)
#print(" "*3,"*"*5)
#number = int(input("Enter the number:"))
#
#for i in range(1,number,2):
#    number=number-1
#    print(" "*number,"*"*i)
#        


#while True:
#    user_input = input("Speak:")
#    if user_input == "stop copying me":
#        break
#    else:
#        while user_input!="stop copying me":
#            print(user_input)
#            break
        

#Guessing game


import random
count = 0

while True:
    rn = random.randint(1,10)
    
    user_input = int(input("Guess the number: "))
    count += 1
    if user_input == rn:
        print("You have guessed it right")
        break
    else:
        if user_input<rn:
            print("Lower than the number!")
        else:
            print("Higher than the number")

    if count==3:
        print("Sorry, you ran out of chances")
        break
























